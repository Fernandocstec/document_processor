from pathlib import Path
import cv2
import numpy as np
from ultralytics import YOLO
import pytesseract
from loguru import logger
from ..core.config import get_settings
from typing import Dict, List, Tuple, Optional
import json

settings = get_settings()

class DocumentProcessor:
    def __init__(self):
        # Inicializa o modelo YOLO e configurações do OCR
        self.model = YOLO(settings.YOLO_MODEL_PATH)
        self.confidence_threshold = settings.CONFIDENCE_THRESHOLD
        self.iou_threshold = settings.IOU_THRESHOLD
        pytesseract.pytesseract.tesseract_cmd = settings.TESSERACT_CMD

    def process_image(self, image_path: Path) -> Dict:
        """
        Processa uma única imagem de documento e extrai texto dos campos detectados.
        """
        logger.info(f"Processando imagem: {image_path}")
        
        # Lê a imagem
        image = cv2.imread(str(image_path))
        if image is None:
            raise ValueError(f"Não foi possível ler a imagem: {image_path}")

        # Executa detecção YOLO
        results = self.model(
            image,
            conf=self.confidence_threshold,
            iou=self.iou_threshold
        )[0]

        # Extrai texto das regiões detectadas
        extracted_data = {}
        for box in results.boxes:
            # Obtém coordenadas e classe
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            class_name = results.names[int(box.cls[0])]
            
            # Recorta a região
            roi = image[y1:y2, x1:x2]
            
            # Aplica OCR
            text = self._extract_text(roi)
            
            # Armazena o resultado
            extracted_data[class_name] = text

        return extracted_data

    def _extract_text(self, image: np.ndarray) -> str:
        """
        Extrai texto de uma região da imagem usando OCR.
        """
        # Pré-processa a imagem
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        # Aplica OCR
        text = pytesseract.image_to_string(
            thresh,
            lang=settings.LANG,
            config='--psm 6'
        )

        return text.strip()

    def process_directory(self, input_dir: Path, output_dir: Path) -> None:
        """
        Processa todas as imagens em um diretório e salva os resultados.
        """
        input_dir = Path(input_dir)
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Obtém todos os arquivos de imagem
        image_files = list(input_dir.glob("*.jpg")) + list(input_dir.glob("*.png"))

        for image_file in image_files:
            try:
                # Processa a imagem
                results = self.process_image(image_file)
                
                # Salva os resultados
                output_file = output_dir / f"{image_file.stem}.json"
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(results, f, ensure_ascii=False, indent=2)
                
                logger.info(f"Processado {image_file.name} -> {output_file.name}")
            
            except Exception as e:
                logger.error(f"Erro ao processar {image_file.name}: {str(e)}")
                continue 
from pathlib import Path
from loguru import logger
from .core.config import get_settings
from .core.logging import setup_logging
from .services.document_processor import DocumentProcessor

def main():
    # Configura o sistema de logging
    logger = setup_logging()
    settings = get_settings()
    
    logger.info(f"Iniciando {settings.APP_NAME} em modo {settings.APP_ENV}")
    
    try:
        # Inicializa o processador de documentos
        processor = DocumentProcessor()
        
        # Processa os documentos
        input_dir = settings.get_input_dir()
        output_dir = settings.get_output_dir()
        
        logger.info(f"Processando documentos de {input_dir}")
        processor.process_directory(input_dir, output_dir)
        logger.info("Processamento de documentos concluído com sucesso")
        
    except Exception as e:
        logger.error(f"Erro durante o processamento de documentos: {str(e)}")
        raise

if __name__ == "__main__":
    main() 
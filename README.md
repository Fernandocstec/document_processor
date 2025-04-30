# Document Processor with YOLOv11 + OCR

Este projeto implementa um pipeline robusto para processamento automático de documentos usando YOLOv11 para detecção de campos e OCR para extração de texto.

## 🚀 Funcionalidades

- Detecção automática de campos em documentos usando YOLOv11
- Extração de texto com OCR otimizado por campo
- Processamento em lote de múltiplos documentos
- Validação semântica de campos extraídos
- Exportação dos dados em formato JSON estruturado
- API REST para processamento de documentos
- Sistema de logging e monitoramento
- Suporte a múltiplos tipos de documentos

## 📋 Pré-requisitos

- Python 3.8+
- Tesseract OCR instalado
- CUDA (opcional, para aceleração GPU)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/document-processor.git
cd document-processor
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

## 🏗️ Estrutura do Projeto

```
document-processor/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── services/
│   └── utils/
├── input_documents/
├── processed_documents/
├── logs/
├── tests/
├── .env
├── requirements.txt
└── README.md
```

## 🚀 Uso

1. Coloque seus documentos na pasta `input_documents/`

2. Execute o processador:
```bash
python -m app.main
```

3. Os resultados serão salvos em `processed_documents/`

## 📊 Resultados

- Redução de mais de 80% no tempo de processamento manual
- Alta precisão na extração de campos-chave
- Pipeline escalável para produção
- Sistema de versionamento e curadoria de erros

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor, leia o guia de contribuição antes de submeter um PR.

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes. 
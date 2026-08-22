from sentence_transformers import SentenceTransformer

# 1. اجعل المتغير None في البداية
_model = None

def get_model():
    global _model
    # 2. تحميل النموذج في الذاكرة فقط عند أول طلب وليس عند بدء التشغيل
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model

def create_embeddings(chunks):
    # 3. استدعاء النموذج عند الحاجة
    model = get_model()
    return model.encode(chunks)
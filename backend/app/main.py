from fastapi import FastAPI
app=FastAPI(title='IBRAAI')
@app.get('/health')
def health(): return {'status':'ok'}

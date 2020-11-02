import uvicorn

if __name__=='__main__':
    uvicorn.run(
        'app:app',
        host='localhost',
        port=3000,
        log_level='info',
        reload=True,
    )
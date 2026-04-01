from fastapi import FastAPI, HTTPException
from .schemas import AuditRequest, AuditResponse
from .services import analyze_code_security

app = FastAPI(title="Sentinel AI Code Auditor", version="1.0")

@app.post("/audit", response_model=AuditResponse)
async def run_audit(request: AuditRequest):
"""
    Submits a code snippet for AI-powered security analysis.
    """
    try:
        # Call to service function to analyze the code security
        result = await analyze_code_security(request.content)
        
        return AuditResponse(
            status="completed",
            vulnerability_score=result["score"],
            findings=result["findings"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

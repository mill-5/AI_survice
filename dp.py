# 수정 전 취약 코드 (일부러 노출)
#API_KEY = "sk-1234567890abcdef"

# 수정 후: 환경 변수 사용으로 변경
import os
API_KEY = os.getenv("OPENAI_API_KEY")

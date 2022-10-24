from fastapi import APIRouter, Body
from app.numverifyApi import numverifyRequest

router = APIRouter()

@router.get('/api/checkPhoneNumber')
def checkPhoneNumber(phone_number:str):
    ans = numverifyRequest(phone_number)
    return ans.text;
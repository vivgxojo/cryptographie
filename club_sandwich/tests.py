import pytest
from main import *

def test_crypter_simple():
    message = "club"
    attendu = "mvel"
    assert crypter_message(message, clef_espion) == attendu

def test_decrypter_simple():
    message_crypte = "mvel"
    attendu = "club"
    assert decrypter_message(message_crypte, clef_espion) == attendu

def test_crypter_et_decrypter_phrase():
    original = "le sandwich est pret"
    crypte = crypter_message(original, clef_espion)
    decode = decrypter_message(crypte, clef_espion)
    assert decode == original

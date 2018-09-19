# -*- coding: utf-8 -*-
'''
Created on 2017-12-20

@author: liuqun
'''
import base64

from alipay.aop.api.constant.CommonConstants import PYTHON_VERSION_3
from alipay.aop.api.exception.Exception import RequestException
from Crypto.Cipher import AES


BLOCK_SIZE = AES.block_size
pad = lambda s, length: s + (BLOCK_SIZE - length % BLOCK_SIZE) * chr(BLOCK_SIZE - length % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def encrypt_content(content, encrypt_type, encrypt_key, charset):
    if "AES" == encrypt_type.upper():
        return aes_encrypt_content(content, encrypt_key, charset)
    raise RequestException("当前不支持该算法类型encrypt_type=" + encrypt_type)


def aes_encrypt_content(content, encrypt_key, charset):
    length = None
    if PYTHON_VERSION_3:
        length = len(bytes(content, encoding=charset))
    else:
        length = len(bytes(content))
    padded_content = pad(content, length)
    iv = '\0' * BLOCK_SIZE
    cryptor = AES.new(base64.b64decode(encrypt_key), AES.MODE_CBC, iv)
    encrypted_content = cryptor.encrypt(padded_content)
    encrypted_content = base64.b64encode(encrypted_content)
    if PYTHON_VERSION_3:
        encrypted_content = str(encrypted_content, encoding=charset)
    return encrypted_content


def decrypt_content(encrypted_content, encrypt_type, encrypt_key, charset):
    if "AES" == encrypt_type.upper():
        return aes_decrypt_content(encrypted_content, encrypt_key, charset)
    raise RequestException("当前不支持该算法类型encrypt_type=" + encrypt_type)


def aes_decrypt_content(encrypted_content, encrypt_key, charset):
    encrypted_content = base64.b64decode(encrypted_content)
    iv = '\0' * BLOCK_SIZE
    cryptor = AES.new(base64.b64decode(encrypt_key), AES.MODE_CBC, iv)
    content = unpad(cryptor.decrypt(encrypted_content))
    if PYTHON_VERSION_3:
        content = content.decode(charset)
    return content

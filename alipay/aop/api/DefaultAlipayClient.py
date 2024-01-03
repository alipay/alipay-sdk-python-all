#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2017-12-20

@author: liuqun
"""
import datetime
import uuid

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.util.WebUtils import *
from alipay.aop.api.util.SignatureUtils import *
from alipay.aop.api.util.CommonUtils import *
from alipay.aop.api.util.EncryptUtils import *

"""
蚂蚁金服开放平台接入客户端
"""
class DefaultAlipayClient(object):

    """
    alipay_client_config：客户端配置，包含app_id、应用私钥、支付宝公钥等
    logger：日志对象，客户端执行信息会通过此日志对象输出
    """
    def __init__(self, alipay_client_config, logger=None):
        self.__config = alipay_client_config
        self.__logger = logger

    """
    内部方法，从params中抽取公共参数
    """
    def __get_common_params(self, params):
        common_params = dict()
        common_params[P_TIMESTAMP] = params[P_TIMESTAMP]
        common_params[P_APP_ID] = self.__config.app_id
        common_params[P_METHOD] = params[P_METHOD]
        common_params[P_CHARSET] = self.__config.charset
        common_params[P_FORMAT] = self.__config.format
        common_params[P_VERSION] = params[P_VERSION]
        common_params[P_SIGN_TYPE] = self.__config.sign_type
        if self.__config.encrypt_type:
            common_params[P_ENCRYPT_TYPE] = self.__config.encrypt_type
        if has_value(params, P_APP_AUTH_TOKEN):
            common_params[P_APP_AUTH_TOKEN] = params[P_APP_AUTH_TOKEN]
        if has_value(params, P_AUTH_TOKEN):
            common_params[P_AUTH_TOKEN] = params[P_AUTH_TOKEN]
        if has_value(params, P_NOTIFY_URL):
            common_params[P_NOTIFY_URL] = params[P_NOTIFY_URL]
        if has_value(params, P_RETURN_URL):
            common_params[P_RETURN_URL] = params[P_RETURN_URL]
        return common_params

    """
    内部方法，从params中移除公共参数
    """
    def __remove_common_params(self, params):
        if not params:
            return
        for k in COMMON_PARAM_KEYS:
            if k in params:
                params.pop(k)

    """
    内部方法，构造form表单输出结果
    """
    def __build_form(self, url, params):
        form = "<form name=\"punchout_form\" method=\"post\" action=\""
        form += url
        form += "\">\n"
        if params:
            for k, v in params.items():
                if not v:
                    continue
                form += "<input type=\"hidden\" name=\""
                form += k
                form += "\" value=\""
                form += v.replace("\"", "&quot;")
                form += "\">\n"
        form += "<input type=\"submit\" value=\"立即支付\" style=\"display:none\" >\n"
        form += "</form>\n"
        form += "<script>document.forms[0].submit();</script>"
        return form

    """
    内部方法，通过请求request对象构造请求查询字符串和业务参数
    """
    def __prepare_request(self, request):
        common_params, params = self.__prepare_request_params(request)
        query_string = url_encode(common_params, self.__config.charset)
        return query_string, params

    """
    内部方法，通过请求request对象构造SDK请求查询字符串
    """
    def __prepare_sdk_request(self, request):
        common_params, params = self.__prepare_request_params(request)
        allParams = dict()
        allParams.update(common_params)
        allParams.update(params)
        query_string = url_encode(allParams, self.__config.charset)
        return query_string

    """
    内部方法，通过请求request对象构造请求参数
    """
    def __prepare_request_params(self, request):
        THREAD_LOCAL.logger = self.__logger
        params = request.get_params()
        if P_BIZ_CONTENT in params:
            if self.__config.encrypt_type and self.__config.encrypt_key:
                params[P_BIZ_CONTENT] = encrypt_content(params[P_BIZ_CONTENT], self.__config.encrypt_type,
                                                        self.__config.encrypt_key, self.__config.charset)
            else:
                if request.need_encrypt:
                    raise RequestException("接口" + params[P_METHOD] + "必须使用encrypt_type、encrypt_key加密")
        params[P_TIMESTAMP] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        common_params = self.__get_common_params(params)
        all_params = dict()
        all_params.update(params)
        all_params.update(common_params)
        sign_content = get_sign_content(all_params)
        sign = ''
        if not self.__config.skip_sign:
            try:
                if self.__config.sign_type and self.__config.sign_type == 'RSA2':
                    sign = sign_with_rsa2(self.__config.app_private_key, sign_content, self.__config.charset)
                else:
                    sign = sign_with_rsa(self.__config.app_private_key, sign_content, self.__config.charset)
            except Exception as e:
                raise RequestException('[' + THREAD_LOCAL.uuid + ']request sign failed. ' + str(e))
            common_params[P_SIGN] = sign
        self.__remove_common_params(params)

        log_url = self.__config.server_url + '?' + sign_content + "&sign=" + sign
        if THREAD_LOCAL.logger:
            THREAD_LOCAL.logger.info('[' + THREAD_LOCAL.uuid + ']request:' + log_url)

        return common_params, params

    """
    内部方法，解析请求返回结果并做验签
    """
    def __parse_response(self, response_str):
        if PYTHON_VERSION_3:
            response_str = response_str.decode(self.__config.charset)
        if THREAD_LOCAL.logger:
            THREAD_LOCAL.logger.info('[' + THREAD_LOCAL.uuid + ']response:' + response_str)

        if self.__config.skip_sign:
            m1 = PATTERN_RESPONSE_BEGIN.search(response_str)
            em1 = PATTERN_RESPONSE_ENCRYPT_BEGIN.search(response_str)
            if not m1 and not em1:
                raise ResponseException('[' + THREAD_LOCAL.uuid + ']response shape maybe illegal. ' + response_str)
            begin_index = 0
            end_index = 0
            has_encrypted = False
            if m1:
                begin_index = m1.end() - 1
                end_index = self.__extract_json_object_end_position(response_str, begin_index)
            elif em1:
                begin_index = em1.end() - 1
                end_index = self.__extract_json_base64_value_end_position(response_str, begin_index)
                has_encrypted = True

            if begin_index >= end_index:
                return response_str

            response_content = response_str[begin_index:end_index]
            if PYTHON_VERSION_3:
                response_content = response_content.encode(self.__config.charset)

            response_content = response_content.decode(self.__config.charset)
            if has_encrypted and self.__config.encrypt_type and self.__config.encrypt_key:
                response_content = decrypt_content(response_content[1:-1], self.__config.encrypt_type,
                                                   self.__config.encrypt_key, self.__config.charset)

            return response_content

        response_content = None
        sign = None
        em1 = None
        em2 = None
        has_encrypted = False
        if self.__config.encrypt_type and self.__config.encrypt_key:
            em1 = PATTERN_RESPONSE_ENCRYPT_BEGIN.search(response_str)
            em2 = PATTERN_RESPONSE_SIGN_ENCRYPT_BEGIN.search(response_str)
            if em1 and em2:
                has_encrypted = True
                sign_start_index = em2.start()
                sign_end_index = em2.end()
                while em2:
                    em2 = PATTERN_RESPONSE_SIGN_BEGIN.search(response_str, pos=em2.end())
                    if em2:
                        sign_start_index = em2.start()
                        sign_end_index = em2.end()
                response_content = response_str[em1.end() - 1:sign_start_index + 1]
                if PYTHON_VERSION_3:
                    response_content = response_content.encode(self.__config.charset)
                sign = response_str[sign_end_index:response_str.find("\"", sign_end_index)]
        if not response_content:
            m1 = PATTERN_RESPONSE_BEGIN.search(response_str)
            m2 = PATTERN_RESPONSE_SIGN_BEGIN.search(response_str)
            if not m1 or not m2:
                raise ResponseException('[' + THREAD_LOCAL.uuid + ']response shape maybe illegal. ' + response_str)
            sign_start_index = m2.start()
            sign_end_index = m2.end()
            while m2:
                m2 = PATTERN_RESPONSE_SIGN_BEGIN.search(response_str, pos=m2.end())
                if m2:
                    sign_start_index = m2.start()
                    sign_end_index = m2.end()
            response_content = response_str[m1.end() - 1:sign_start_index + 1]
            if PYTHON_VERSION_3:
                response_content = response_content.encode(self.__config.charset)
            sign = response_str[sign_end_index:response_str.find("\"", sign_end_index)]
        try:
            verify_res = verify_with_rsa(self.__config.alipay_public_key, response_content, sign)
        except Exception as e:
            raise ResponseException('[' + THREAD_LOCAL.uuid + ']response sign verify failed. ' + str(e) + \
                                    ' ' + response_str)
        if not verify_res:
            raise ResponseException('[' + THREAD_LOCAL.uuid + ']response sign verify failed. ' + response_str)
        response_content = response_content.decode(self.__config.charset)
        if has_encrypted:
            response_content = decrypt_content(response_content[1:-1], self.__config.encrypt_type,
                                               self.__config.encrypt_key, self.__config.charset)
        return response_content

    '''
    提取密文验签内容终点
    '''
    def __extract_json_base64_value_end_position(self, response_string, begin_position):
        for index in range(begin_position, len(response_string)):
            # 找到第2个双引号作为终点，由于中间全部是Base64编码的密文，所以不会有干扰的特殊字符
            if response_string[index] == '"' and index != begin_position:
                return index + 1

        # 如果没有找到第2个双引号，说明验签内容片段提取失败，直接尝试选取剩余整个响应字符串进行验签
        return len(response_string)

    '''
    提取明文验签内容终点
    '''
    def __extract_json_object_end_position(self, response_string, begin_position):
        # 记录当前尚未发现配对闭合的大括号
        braces = []
        # 记录当前字符是否在双引号中
        in_quotes = False
        # 记录当前字符前面连续的转义字符个数
        consecutive_escape_count = 0

        # 从待验签字符的起点开始遍历后续字符串，找出待验签字符串的终止点，终点即是与起点{配对的}
        for index in range(begin_position, len(response_string)):
            # 提取当前字符
            current_char = response_string[index]

            # 如果当前字符是"且前面有偶数个转义标记（0也是偶数）
            if current_char == '"' and consecutive_escape_count % 2 == 0:
                # 是否在引号中的状态取反
                in_quotes = not in_quotes

            # 如果当前字符是{且不在引号中
            elif current_char == '{' and not in_quotes:
                # 将该{加入未闭合括号中
                braces.append("{")

            # 如果当前字符是}且不在引号中
            elif current_char == '}' and not in_quotes:
                # 弹出一个未闭合括号
                braces.pop()
                # 如果弹出后，未闭合括号为空，说明已经找到终点
                if len(braces) == 0:
                    return index + 1

            # 如果当前字符是转义字符
            if current_char == '\\':
                # 连续转义字符个数+1
                consecutive_escape_count += 1
            else:
                # 连续转义字符个数置0
                consecutive_escape_count = 0

        # 如果没有找到配对的闭合括号，说明验签内容片段提取失败，直接尝试选取剩余整个响应字符串进行验签
        return len(response_string)

    """
    执行接口请求
    """
    def execute(self, request):
        THREAD_LOCAL.uuid = str(uuid.uuid1())
        headers = {
            'Content-type': 'application/x-www-form-urlencoded;charset=' + self.__config.charset,
            "Cache-Control": "no-cache",
            "Connection": "Keep-Alive",
            "User-Agent": ALIPAY_SDK_PYTHON_VERSION,
            "log-uuid": THREAD_LOCAL.uuid,
        }

        query_string, params = self.__prepare_request(request)
        multipart_params = request.get_multipart_params()

        if multipart_params and len(multipart_params) > 0:
            response = do_multipart_post(self.__config.server_url, query_string, headers, params, multipart_params,
                                         self.__config.charset, self.__config.timeout)
        else:
            response = do_post(self.__config.server_url, query_string, headers, params, self.__config.charset,
                               self.__config.timeout)

        return self.__parse_response(response)

    '''
    得到页面跳转接口的url或表单html
    '''
    def page_execute(self, request, http_method="POST"):
        THREAD_LOCAL.uuid = str(uuid.uuid1())
        url = self.__config.server_url
        pos = url.find("?")
        if pos >= 0:
            url = url[0:pos]

        query_string, params = self.__prepare_request(request)

        if http_method == "GET":
            return url + "?" + query_string + "&" + url_encode(params, self.__config.charset)
        else:
            return self.__build_form(url + "?" + query_string, params)

    '''
    得到sdk调用的参数
    '''
    def sdk_execute(self, request):
        THREAD_LOCAL.uuid = str(uuid.uuid1())
        return self.__prepare_sdk_request(request)
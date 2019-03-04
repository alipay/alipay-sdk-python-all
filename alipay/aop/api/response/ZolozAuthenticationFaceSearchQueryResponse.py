#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FaceSearchResult import FaceSearchResult
from alipay.aop.api.domain.FaceSearchResult import FaceSearchResult


class ZolozAuthenticationFaceSearchQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZolozAuthenticationFaceSearchQueryResponse, self).__init__()
        self._candidate_list = None
        self._found_face = None
        self._ret_code_sub = None
        self._ret_message_sub = None

    @property
    def candidate_list(self):
        return self._candidate_list

    @candidate_list.setter
    def candidate_list(self, value):
        if isinstance(value, list):
            self._candidate_list = list()
            for i in value:
                if isinstance(i, FaceSearchResult):
                    self._candidate_list.append(i)
                else:
                    self._candidate_list.append(FaceSearchResult.from_alipay_dict(i))
    @property
    def found_face(self):
        return self._found_face

    @found_face.setter
    def found_face(self, value):
        if isinstance(value, FaceSearchResult):
            self._found_face = value
        else:
            self._found_face = FaceSearchResult.from_alipay_dict(value)
    @property
    def ret_code_sub(self):
        return self._ret_code_sub

    @ret_code_sub.setter
    def ret_code_sub(self, value):
        self._ret_code_sub = value
    @property
    def ret_message_sub(self):
        return self._ret_message_sub

    @ret_message_sub.setter
    def ret_message_sub(self, value):
        self._ret_message_sub = value

    def parse_response_content(self, response_content):
        response = super(ZolozAuthenticationFaceSearchQueryResponse, self).parse_response_content(response_content)
        if 'candidate_list' in response:
            self.candidate_list = response['candidate_list']
        if 'found_face' in response:
            self.found_face = response['found_face']
        if 'ret_code_sub' in response:
            self.ret_code_sub = response['ret_code_sub']
        if 'ret_message_sub' in response:
            self.ret_message_sub = response['ret_message_sub']

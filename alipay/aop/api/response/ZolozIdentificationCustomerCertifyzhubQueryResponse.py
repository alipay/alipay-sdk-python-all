#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FaceAttrInfo import FaceAttrInfo


class ZolozIdentificationCustomerCertifyzhubQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZolozIdentificationCustomerCertifyzhubQueryResponse, self).__init__()
        self._attack = None
        self._biz_id = None
        self._face_attr_info = None
        self._img_str = None
        self._zim_code = None
        self._zim_msg = None

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        self._attack = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def face_attr_info(self):
        return self._face_attr_info

    @face_attr_info.setter
    def face_attr_info(self, value):
        if isinstance(value, FaceAttrInfo):
            self._face_attr_info = value
        else:
            self._face_attr_info = FaceAttrInfo.from_alipay_dict(value)
    @property
    def img_str(self):
        return self._img_str

    @img_str.setter
    def img_str(self, value):
        self._img_str = value
    @property
    def zim_code(self):
        return self._zim_code

    @zim_code.setter
    def zim_code(self, value):
        self._zim_code = value
    @property
    def zim_msg(self):
        return self._zim_msg

    @zim_msg.setter
    def zim_msg(self, value):
        self._zim_msg = value

    def parse_response_content(self, response_content):
        response = super(ZolozIdentificationCustomerCertifyzhubQueryResponse, self).parse_response_content(response_content)
        if 'attack' in response:
            self.attack = response['attack']
        if 'biz_id' in response:
            self.biz_id = response['biz_id']
        if 'face_attr_info' in response:
            self.face_attr_info = response['face_attr_info']
        if 'img_str' in response:
            self.img_str = response['img_str']
        if 'zim_code' in response:
            self.zim_code = response['zim_code']
        if 'zim_msg' in response:
            self.zim_msg = response['zim_msg']

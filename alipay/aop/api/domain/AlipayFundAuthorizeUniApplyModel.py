#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AuthBizParam import AuthBizParam
from alipay.aop.api.domain.AuthParticipantInfo import AuthParticipantInfo
from alipay.aop.api.domain.AuthParticipantInfo import AuthParticipantInfo
from alipay.aop.api.domain.AuthParticipantInfo import AuthParticipantInfo


class AlipayFundAuthorizeUniApplyModel(object):

    def __init__(self):
        self._apply_expire_time = None
        self._auth_biz_param = None
        self._auth_expire_time = None
        self._authorize_link_type = None
        self._biz_scene = None
        self._channel = None
        self._out_biz_no = None
        self._partner_info = None
        self._principal_info = None
        self._product_code = None
        self._sub_biz_scene = None
        self._third_party_info = None

    @property
    def apply_expire_time(self):
        return self._apply_expire_time

    @apply_expire_time.setter
    def apply_expire_time(self, value):
        self._apply_expire_time = value
    @property
    def auth_biz_param(self):
        return self._auth_biz_param

    @auth_biz_param.setter
    def auth_biz_param(self, value):
        if isinstance(value, AuthBizParam):
            self._auth_biz_param = value
        else:
            self._auth_biz_param = AuthBizParam.from_alipay_dict(value)
    @property
    def auth_expire_time(self):
        return self._auth_expire_time

    @auth_expire_time.setter
    def auth_expire_time(self, value):
        self._auth_expire_time = value
    @property
    def authorize_link_type(self):
        return self._authorize_link_type

    @authorize_link_type.setter
    def authorize_link_type(self, value):
        self._authorize_link_type = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_info(self):
        return self._partner_info

    @partner_info.setter
    def partner_info(self, value):
        if isinstance(value, AuthParticipantInfo):
            self._partner_info = value
        else:
            self._partner_info = AuthParticipantInfo.from_alipay_dict(value)
    @property
    def principal_info(self):
        return self._principal_info

    @principal_info.setter
    def principal_info(self, value):
        if isinstance(value, AuthParticipantInfo):
            self._principal_info = value
        else:
            self._principal_info = AuthParticipantInfo.from_alipay_dict(value)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def sub_biz_scene(self):
        return self._sub_biz_scene

    @sub_biz_scene.setter
    def sub_biz_scene(self, value):
        self._sub_biz_scene = value
    @property
    def third_party_info(self):
        return self._third_party_info

    @third_party_info.setter
    def third_party_info(self, value):
        if isinstance(value, AuthParticipantInfo):
            self._third_party_info = value
        else:
            self._third_party_info = AuthParticipantInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.apply_expire_time:
            if hasattr(self.apply_expire_time, 'to_alipay_dict'):
                params['apply_expire_time'] = self.apply_expire_time.to_alipay_dict()
            else:
                params['apply_expire_time'] = self.apply_expire_time
        if self.auth_biz_param:
            if hasattr(self.auth_biz_param, 'to_alipay_dict'):
                params['auth_biz_param'] = self.auth_biz_param.to_alipay_dict()
            else:
                params['auth_biz_param'] = self.auth_biz_param
        if self.auth_expire_time:
            if hasattr(self.auth_expire_time, 'to_alipay_dict'):
                params['auth_expire_time'] = self.auth_expire_time.to_alipay_dict()
            else:
                params['auth_expire_time'] = self.auth_expire_time
        if self.authorize_link_type:
            if hasattr(self.authorize_link_type, 'to_alipay_dict'):
                params['authorize_link_type'] = self.authorize_link_type.to_alipay_dict()
            else:
                params['authorize_link_type'] = self.authorize_link_type
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_info:
            if hasattr(self.partner_info, 'to_alipay_dict'):
                params['partner_info'] = self.partner_info.to_alipay_dict()
            else:
                params['partner_info'] = self.partner_info
        if self.principal_info:
            if hasattr(self.principal_info, 'to_alipay_dict'):
                params['principal_info'] = self.principal_info.to_alipay_dict()
            else:
                params['principal_info'] = self.principal_info
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.sub_biz_scene:
            if hasattr(self.sub_biz_scene, 'to_alipay_dict'):
                params['sub_biz_scene'] = self.sub_biz_scene.to_alipay_dict()
            else:
                params['sub_biz_scene'] = self.sub_biz_scene
        if self.third_party_info:
            if hasattr(self.third_party_info, 'to_alipay_dict'):
                params['third_party_info'] = self.third_party_info.to_alipay_dict()
            else:
                params['third_party_info'] = self.third_party_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundAuthorizeUniApplyModel()
        if 'apply_expire_time' in d:
            o.apply_expire_time = d['apply_expire_time']
        if 'auth_biz_param' in d:
            o.auth_biz_param = d['auth_biz_param']
        if 'auth_expire_time' in d:
            o.auth_expire_time = d['auth_expire_time']
        if 'authorize_link_type' in d:
            o.authorize_link_type = d['authorize_link_type']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'channel' in d:
            o.channel = d['channel']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_info' in d:
            o.partner_info = d['partner_info']
        if 'principal_info' in d:
            o.principal_info = d['principal_info']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'sub_biz_scene' in d:
            o.sub_biz_scene = d['sub_biz_scene']
        if 'third_party_info' in d:
            o.third_party_info = d['third_party_info']
        return o



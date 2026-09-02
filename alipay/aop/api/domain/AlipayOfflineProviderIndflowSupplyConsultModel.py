#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndflowBizInfo import IndflowBizInfo


class AlipayOfflineProviderIndflowSupplyConsultModel(object):

    def __init__(self):
        self._biz_info = None
        self._mobile_phone = None
        self._out_pos_id = None
        self._style_type = None

    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        if isinstance(value, IndflowBizInfo):
            self._biz_info = value
        else:
            self._biz_info = IndflowBizInfo.from_alipay_dict(value)
    @property
    def mobile_phone(self):
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value):
        self._mobile_phone = value
    @property
    def out_pos_id(self):
        return self._out_pos_id

    @out_pos_id.setter
    def out_pos_id(self, value):
        self._out_pos_id = value
    @property
    def style_type(self):
        return self._style_type

    @style_type.setter
    def style_type(self, value):
        self._style_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_info:
            if hasattr(self.biz_info, 'to_alipay_dict'):
                params['biz_info'] = self.biz_info.to_alipay_dict()
            else:
                params['biz_info'] = self.biz_info
        if self.mobile_phone:
            if hasattr(self.mobile_phone, 'to_alipay_dict'):
                params['mobile_phone'] = self.mobile_phone.to_alipay_dict()
            else:
                params['mobile_phone'] = self.mobile_phone
        if self.out_pos_id:
            if hasattr(self.out_pos_id, 'to_alipay_dict'):
                params['out_pos_id'] = self.out_pos_id.to_alipay_dict()
            else:
                params['out_pos_id'] = self.out_pos_id
        if self.style_type:
            if hasattr(self.style_type, 'to_alipay_dict'):
                params['style_type'] = self.style_type.to_alipay_dict()
            else:
                params['style_type'] = self.style_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderIndflowSupplyConsultModel()
        if 'biz_info' in d:
            o.biz_info = d['biz_info']
        if 'mobile_phone' in d:
            o.mobile_phone = d['mobile_phone']
        if 'out_pos_id' in d:
            o.out_pos_id = d['out_pos_id']
        if 'style_type' in d:
            o.style_type = d['style_type']
        return o



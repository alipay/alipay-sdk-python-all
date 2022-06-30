#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CertifyConfig import CertifyConfig
from alipay.aop.api.domain.ScenicExtInfo import ScenicExtInfo
from alipay.aop.api.domain.PsbHotelInfo import PsbHotelInfo


class AlipayCommerceDataHotelVerifySyncModel(object):

    def __init__(self):
        self._certify_config = None
        self._code_values = None
        self._ext_info = None
        self._psb_hotel_info = None
        self._shop_id = None
        self._source_code = None

    @property
    def certify_config(self):
        return self._certify_config

    @certify_config.setter
    def certify_config(self, value):
        if isinstance(value, CertifyConfig):
            self._certify_config = value
        else:
            self._certify_config = CertifyConfig.from_alipay_dict(value)
    @property
    def code_values(self):
        return self._code_values

    @code_values.setter
    def code_values(self, value):
        self._code_values = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, ScenicExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(ScenicExtInfo.from_alipay_dict(i))
    @property
    def psb_hotel_info(self):
        return self._psb_hotel_info

    @psb_hotel_info.setter
    def psb_hotel_info(self, value):
        if isinstance(value, PsbHotelInfo):
            self._psb_hotel_info = value
        else:
            self._psb_hotel_info = PsbHotelInfo.from_alipay_dict(value)
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def source_code(self):
        return self._source_code

    @source_code.setter
    def source_code(self, value):
        self._source_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.certify_config:
            if hasattr(self.certify_config, 'to_alipay_dict'):
                params['certify_config'] = self.certify_config.to_alipay_dict()
            else:
                params['certify_config'] = self.certify_config
        if self.code_values:
            if hasattr(self.code_values, 'to_alipay_dict'):
                params['code_values'] = self.code_values.to_alipay_dict()
            else:
                params['code_values'] = self.code_values
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.psb_hotel_info:
            if hasattr(self.psb_hotel_info, 'to_alipay_dict'):
                params['psb_hotel_info'] = self.psb_hotel_info.to_alipay_dict()
            else:
                params['psb_hotel_info'] = self.psb_hotel_info
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.source_code:
            if hasattr(self.source_code, 'to_alipay_dict'):
                params['source_code'] = self.source_code.to_alipay_dict()
            else:
                params['source_code'] = self.source_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceDataHotelVerifySyncModel()
        if 'certify_config' in d:
            o.certify_config = d['certify_config']
        if 'code_values' in d:
            o.code_values = d['code_values']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'psb_hotel_info' in d:
            o.psb_hotel_info = d['psb_hotel_info']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'source_code' in d:
            o.source_code = d['source_code']
        return o



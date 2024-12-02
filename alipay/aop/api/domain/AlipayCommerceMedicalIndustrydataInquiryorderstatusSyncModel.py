#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PlatformInquiryOrderStatusExtInfo import PlatformInquiryOrderStatusExtInfo


class AlipayCommerceMedicalIndustrydataInquiryorderstatusSyncModel(object):

    def __init__(self):
        self._alipay_open_id = None
        self._alipay_order_id = None
        self._alipay_user_id = None
        self._ext_info = None
        self._merchant_order_status = None
        self._merchant_user_id = None
        self._out_biz_no = None
        self._platform_code = None

    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def alipay_order_id(self):
        return self._alipay_order_id

    @alipay_order_id.setter
    def alipay_order_id(self, value):
        self._alipay_order_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, PlatformInquiryOrderStatusExtInfo):
            self._ext_info = value
        else:
            self._ext_info = PlatformInquiryOrderStatusExtInfo.from_alipay_dict(value)
    @property
    def merchant_order_status(self):
        return self._merchant_order_status

    @merchant_order_status.setter
    def merchant_order_status(self, value):
        self._merchant_order_status = value
    @property
    def merchant_user_id(self):
        return self._merchant_user_id

    @merchant_user_id.setter
    def merchant_user_id(self, value):
        self._merchant_user_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.alipay_order_id:
            if hasattr(self.alipay_order_id, 'to_alipay_dict'):
                params['alipay_order_id'] = self.alipay_order_id.to_alipay_dict()
            else:
                params['alipay_order_id'] = self.alipay_order_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.merchant_order_status:
            if hasattr(self.merchant_order_status, 'to_alipay_dict'):
                params['merchant_order_status'] = self.merchant_order_status.to_alipay_dict()
            else:
                params['merchant_order_status'] = self.merchant_order_status
        if self.merchant_user_id:
            if hasattr(self.merchant_user_id, 'to_alipay_dict'):
                params['merchant_user_id'] = self.merchant_user_id.to_alipay_dict()
            else:
                params['merchant_user_id'] = self.merchant_user_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIndustrydataInquiryorderstatusSyncModel()
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'alipay_order_id' in d:
            o.alipay_order_id = d['alipay_order_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'merchant_order_status' in d:
            o.merchant_order_status = d['merchant_order_status']
        if 'merchant_user_id' in d:
            o.merchant_user_id = d['merchant_user_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        return o



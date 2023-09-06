#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CertificateUseInfo import CertificateUseInfo


class AlipayMarketingCertificateCertificationUseModel(object):

    def __init__(self):
        self._biz_dt = None
        self._certificate_use_info_list = None
        self._code = None
        self._open_id = None
        self._order_id = None
        self._out_biz_no = None
        self._out_order_id = None
        self._shop_id = None
        self._user_id = None

    @property
    def biz_dt(self):
        return self._biz_dt

    @biz_dt.setter
    def biz_dt(self, value):
        self._biz_dt = value
    @property
    def certificate_use_info_list(self):
        return self._certificate_use_info_list

    @certificate_use_info_list.setter
    def certificate_use_info_list(self, value):
        if isinstance(value, list):
            self._certificate_use_info_list = list()
            for i in value:
                if isinstance(i, CertificateUseInfo):
                    self._certificate_use_info_list.append(i)
                else:
                    self._certificate_use_info_list.append(CertificateUseInfo.from_alipay_dict(i))
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_dt:
            if hasattr(self.biz_dt, 'to_alipay_dict'):
                params['biz_dt'] = self.biz_dt.to_alipay_dict()
            else:
                params['biz_dt'] = self.biz_dt
        if self.certificate_use_info_list:
            if isinstance(self.certificate_use_info_list, list):
                for i in range(0, len(self.certificate_use_info_list)):
                    element = self.certificate_use_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.certificate_use_info_list[i] = element.to_alipay_dict()
            if hasattr(self.certificate_use_info_list, 'to_alipay_dict'):
                params['certificate_use_info_list'] = self.certificate_use_info_list.to_alipay_dict()
            else:
                params['certificate_use_info_list'] = self.certificate_use_info_list
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCertificateCertificationUseModel()
        if 'biz_dt' in d:
            o.biz_dt = d['biz_dt']
        if 'certificate_use_info_list' in d:
            o.certificate_use_info_list = d['certificate_use_info_list']
        if 'code' in d:
            o.code = d['code']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



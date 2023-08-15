#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniOrderSelfitembillBatchqueryModel(object):

    def __init__(self):
        self._certificate_id = None
        self._certificate_status = None
        self._mini_app_id = None
        self._page_num = None
        self._page_size = None
        self._serial_no = None
        self._settle_status = None
        self._settlement_date = None
        self._verification_shop_id = None
        self._verify_date = None

    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def certificate_status(self):
        return self._certificate_status

    @certificate_status.setter
    def certificate_status(self, value):
        self._certificate_status = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def settle_status(self):
        return self._settle_status

    @settle_status.setter
    def settle_status(self, value):
        self._settle_status = value
    @property
    def settlement_date(self):
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, value):
        self._settlement_date = value
    @property
    def verification_shop_id(self):
        return self._verification_shop_id

    @verification_shop_id.setter
    def verification_shop_id(self, value):
        self._verification_shop_id = value
    @property
    def verify_date(self):
        return self._verify_date

    @verify_date.setter
    def verify_date(self, value):
        self._verify_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.certificate_status:
            if hasattr(self.certificate_status, 'to_alipay_dict'):
                params['certificate_status'] = self.certificate_status.to_alipay_dict()
            else:
                params['certificate_status'] = self.certificate_status
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.settle_status:
            if hasattr(self.settle_status, 'to_alipay_dict'):
                params['settle_status'] = self.settle_status.to_alipay_dict()
            else:
                params['settle_status'] = self.settle_status
        if self.settlement_date:
            if hasattr(self.settlement_date, 'to_alipay_dict'):
                params['settlement_date'] = self.settlement_date.to_alipay_dict()
            else:
                params['settlement_date'] = self.settlement_date
        if self.verification_shop_id:
            if hasattr(self.verification_shop_id, 'to_alipay_dict'):
                params['verification_shop_id'] = self.verification_shop_id.to_alipay_dict()
            else:
                params['verification_shop_id'] = self.verification_shop_id
        if self.verify_date:
            if hasattr(self.verify_date, 'to_alipay_dict'):
                params['verify_date'] = self.verify_date.to_alipay_dict()
            else:
                params['verify_date'] = self.verify_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniOrderSelfitembillBatchqueryModel()
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'certificate_status' in d:
            o.certificate_status = d['certificate_status']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'settle_status' in d:
            o.settle_status = d['settle_status']
        if 'settlement_date' in d:
            o.settlement_date = d['settlement_date']
        if 'verification_shop_id' in d:
            o.verification_shop_id = d['verification_shop_id']
        if 'verify_date' in d:
            o.verify_date = d['verify_date']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppMerchantExternalbillCreateModel(object):

    def __init__(self):
        self._bill_amount = None
        self._bill_date_desc = None
        self._bill_date_end = None
        self._bill_date_start = None
        self._biz_type = None
        self._expiry_date = None
        self._fee_type = None
        self._fine_amount = None
        self._fine_date = None
        self._memo = None
        self._merchant_code = None
        self._object_id = None
        self._out_biz_no = None
        self._release_date = None
        self._select_optional = None
        self._sequence = None
        self._service_amount = None
        self._sub_biz_type = None
        self._total_amount = None

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def bill_date_desc(self):
        return self._bill_date_desc

    @bill_date_desc.setter
    def bill_date_desc(self, value):
        self._bill_date_desc = value
    @property
    def bill_date_end(self):
        return self._bill_date_end

    @bill_date_end.setter
    def bill_date_end(self, value):
        self._bill_date_end = value
    @property
    def bill_date_start(self):
        return self._bill_date_start

    @bill_date_start.setter
    def bill_date_start(self, value):
        self._bill_date_start = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self._expiry_date = value
    @property
    def fee_type(self):
        return self._fee_type

    @fee_type.setter
    def fee_type(self, value):
        self._fee_type = value
    @property
    def fine_amount(self):
        return self._fine_amount

    @fine_amount.setter
    def fine_amount(self, value):
        self._fine_amount = value
    @property
    def fine_date(self):
        return self._fine_date

    @fine_date.setter
    def fine_date(self, value):
        self._fine_date = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def merchant_code(self):
        return self._merchant_code

    @merchant_code.setter
    def merchant_code(self, value):
        self._merchant_code = value
    @property
    def object_id(self):
        return self._object_id

    @object_id.setter
    def object_id(self, value):
        self._object_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, value):
        self._release_date = value
    @property
    def select_optional(self):
        return self._select_optional

    @select_optional.setter
    def select_optional(self, value):
        self._select_optional = value
    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        self._sequence = value
    @property
    def service_amount(self):
        return self._service_amount

    @service_amount.setter
    def service_amount(self, value):
        self._service_amount = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
        if self.bill_date_desc:
            if hasattr(self.bill_date_desc, 'to_alipay_dict'):
                params['bill_date_desc'] = self.bill_date_desc.to_alipay_dict()
            else:
                params['bill_date_desc'] = self.bill_date_desc
        if self.bill_date_end:
            if hasattr(self.bill_date_end, 'to_alipay_dict'):
                params['bill_date_end'] = self.bill_date_end.to_alipay_dict()
            else:
                params['bill_date_end'] = self.bill_date_end
        if self.bill_date_start:
            if hasattr(self.bill_date_start, 'to_alipay_dict'):
                params['bill_date_start'] = self.bill_date_start.to_alipay_dict()
            else:
                params['bill_date_start'] = self.bill_date_start
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.expiry_date:
            if hasattr(self.expiry_date, 'to_alipay_dict'):
                params['expiry_date'] = self.expiry_date.to_alipay_dict()
            else:
                params['expiry_date'] = self.expiry_date
        if self.fee_type:
            if hasattr(self.fee_type, 'to_alipay_dict'):
                params['fee_type'] = self.fee_type.to_alipay_dict()
            else:
                params['fee_type'] = self.fee_type
        if self.fine_amount:
            if hasattr(self.fine_amount, 'to_alipay_dict'):
                params['fine_amount'] = self.fine_amount.to_alipay_dict()
            else:
                params['fine_amount'] = self.fine_amount
        if self.fine_date:
            if hasattr(self.fine_date, 'to_alipay_dict'):
                params['fine_date'] = self.fine_date.to_alipay_dict()
            else:
                params['fine_date'] = self.fine_date
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.merchant_code:
            if hasattr(self.merchant_code, 'to_alipay_dict'):
                params['merchant_code'] = self.merchant_code.to_alipay_dict()
            else:
                params['merchant_code'] = self.merchant_code
        if self.object_id:
            if hasattr(self.object_id, 'to_alipay_dict'):
                params['object_id'] = self.object_id.to_alipay_dict()
            else:
                params['object_id'] = self.object_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.release_date:
            if hasattr(self.release_date, 'to_alipay_dict'):
                params['release_date'] = self.release_date.to_alipay_dict()
            else:
                params['release_date'] = self.release_date
        if self.select_optional:
            if hasattr(self.select_optional, 'to_alipay_dict'):
                params['select_optional'] = self.select_optional.to_alipay_dict()
            else:
                params['select_optional'] = self.select_optional
        if self.sequence:
            if hasattr(self.sequence, 'to_alipay_dict'):
                params['sequence'] = self.sequence.to_alipay_dict()
            else:
                params['sequence'] = self.sequence
        if self.service_amount:
            if hasattr(self.service_amount, 'to_alipay_dict'):
                params['service_amount'] = self.service_amount.to_alipay_dict()
            else:
                params['service_amount'] = self.service_amount
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppMerchantExternalbillCreateModel()
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'bill_date_desc' in d:
            o.bill_date_desc = d['bill_date_desc']
        if 'bill_date_end' in d:
            o.bill_date_end = d['bill_date_end']
        if 'bill_date_start' in d:
            o.bill_date_start = d['bill_date_start']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'expiry_date' in d:
            o.expiry_date = d['expiry_date']
        if 'fee_type' in d:
            o.fee_type = d['fee_type']
        if 'fine_amount' in d:
            o.fine_amount = d['fine_amount']
        if 'fine_date' in d:
            o.fine_date = d['fine_date']
        if 'memo' in d:
            o.memo = d['memo']
        if 'merchant_code' in d:
            o.merchant_code = d['merchant_code']
        if 'object_id' in d:
            o.object_id = d['object_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'release_date' in d:
            o.release_date = d['release_date']
        if 'select_optional' in d:
            o.select_optional = d['select_optional']
        if 'sequence' in d:
            o.sequence = d['sequence']
        if 'service_amount' in d:
            o.service_amount = d['service_amount']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o



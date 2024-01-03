#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceAnthotlinemngCalldetailBatchqueryModel(object):

    def __init__(self):
        self._biz_code = None
        self._biz_sign = None
        self._called_number = None
        self._calling_number = None
        self._contact_id = None
        self._contact_type = None
        self._end_time = None
        self._instance_id = None
        self._page_num = None
        self._page_size = None
        self._sort_order = None
        self._start_time = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_sign(self):
        return self._biz_sign

    @biz_sign.setter
    def biz_sign(self, value):
        self._biz_sign = value
    @property
    def called_number(self):
        return self._called_number

    @called_number.setter
    def called_number(self, value):
        self._called_number = value
    @property
    def calling_number(self):
        return self._calling_number

    @calling_number.setter
    def calling_number(self, value):
        self._calling_number = value
    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, value):
        self._contact_id = value
    @property
    def contact_type(self):
        return self._contact_type

    @contact_type.setter
    def contact_type(self, value):
        self._contact_type = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = value
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
    def sort_order(self):
        return self._sort_order

    @sort_order.setter
    def sort_order(self, value):
        self._sort_order = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_sign:
            if hasattr(self.biz_sign, 'to_alipay_dict'):
                params['biz_sign'] = self.biz_sign.to_alipay_dict()
            else:
                params['biz_sign'] = self.biz_sign
        if self.called_number:
            if hasattr(self.called_number, 'to_alipay_dict'):
                params['called_number'] = self.called_number.to_alipay_dict()
            else:
                params['called_number'] = self.called_number
        if self.calling_number:
            if hasattr(self.calling_number, 'to_alipay_dict'):
                params['calling_number'] = self.calling_number.to_alipay_dict()
            else:
                params['calling_number'] = self.calling_number
        if self.contact_id:
            if hasattr(self.contact_id, 'to_alipay_dict'):
                params['contact_id'] = self.contact_id.to_alipay_dict()
            else:
                params['contact_id'] = self.contact_id
        if self.contact_type:
            if hasattr(self.contact_type, 'to_alipay_dict'):
                params['contact_type'] = self.contact_type.to_alipay_dict()
            else:
                params['contact_type'] = self.contact_type
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.instance_id:
            if hasattr(self.instance_id, 'to_alipay_dict'):
                params['instance_id'] = self.instance_id.to_alipay_dict()
            else:
                params['instance_id'] = self.instance_id
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
        if self.sort_order:
            if hasattr(self.sort_order, 'to_alipay_dict'):
                params['sort_order'] = self.sort_order.to_alipay_dict()
            else:
                params['sort_order'] = self.sort_order
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceAnthotlinemngCalldetailBatchqueryModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_sign' in d:
            o.biz_sign = d['biz_sign']
        if 'called_number' in d:
            o.called_number = d['called_number']
        if 'calling_number' in d:
            o.calling_number = d['calling_number']
        if 'contact_id' in d:
            o.contact_id = d['contact_id']
        if 'contact_type' in d:
            o.contact_type = d['contact_type']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'instance_id' in d:
            o.instance_id = d['instance_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'sort_order' in d:
            o.sort_order = d['sort_order']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o



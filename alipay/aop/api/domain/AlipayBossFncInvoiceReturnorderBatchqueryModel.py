#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncInvoiceReturnorderBatchqueryModel(object):

    def __init__(self):
        self._apply_date_begin = None
        self._apply_date_end = None
        self._inst_id = None
        self._invoice_code = None
        self._invoice_no = None
        self._invoice_open_date_begin = None
        self._invoice_open_date_end = None
        self._invoice_types = None
        self._ip_id = None
        self._ip_role_id = None
        self._order_nos = None
        self._order_status = None
        self._order_type = None
        self._page_no = None
        self._page_size = None
        self._return_reason_types = None
        self._source = None
        self._tracking_no = None

    @property
    def apply_date_begin(self):
        return self._apply_date_begin

    @apply_date_begin.setter
    def apply_date_begin(self, value):
        self._apply_date_begin = value
    @property
    def apply_date_end(self):
        return self._apply_date_end

    @apply_date_end.setter
    def apply_date_end(self, value):
        self._apply_date_end = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def invoice_code(self):
        return self._invoice_code

    @invoice_code.setter
    def invoice_code(self, value):
        self._invoice_code = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_open_date_begin(self):
        return self._invoice_open_date_begin

    @invoice_open_date_begin.setter
    def invoice_open_date_begin(self, value):
        self._invoice_open_date_begin = value
    @property
    def invoice_open_date_end(self):
        return self._invoice_open_date_end

    @invoice_open_date_end.setter
    def invoice_open_date_end(self, value):
        self._invoice_open_date_end = value
    @property
    def invoice_types(self):
        return self._invoice_types

    @invoice_types.setter
    def invoice_types(self, value):
        if isinstance(value, list):
            self._invoice_types = list()
            for i in value:
                self._invoice_types.append(i)
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def order_nos(self):
        return self._order_nos

    @order_nos.setter
    def order_nos(self, value):
        if isinstance(value, list):
            self._order_nos = list()
            for i in value:
                self._order_nos.append(i)
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        if isinstance(value, list):
            self._order_status = list()
            for i in value:
                self._order_status.append(i)
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def return_reason_types(self):
        return self._return_reason_types

    @return_reason_types.setter
    def return_reason_types(self, value):
        if isinstance(value, list):
            self._return_reason_types = list()
            for i in value:
                self._return_reason_types.append(i)
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def tracking_no(self):
        return self._tracking_no

    @tracking_no.setter
    def tracking_no(self, value):
        self._tracking_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_date_begin:
            if hasattr(self.apply_date_begin, 'to_alipay_dict'):
                params['apply_date_begin'] = self.apply_date_begin.to_alipay_dict()
            else:
                params['apply_date_begin'] = self.apply_date_begin
        if self.apply_date_end:
            if hasattr(self.apply_date_end, 'to_alipay_dict'):
                params['apply_date_end'] = self.apply_date_end.to_alipay_dict()
            else:
                params['apply_date_end'] = self.apply_date_end
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.invoice_code:
            if hasattr(self.invoice_code, 'to_alipay_dict'):
                params['invoice_code'] = self.invoice_code.to_alipay_dict()
            else:
                params['invoice_code'] = self.invoice_code
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_open_date_begin:
            if hasattr(self.invoice_open_date_begin, 'to_alipay_dict'):
                params['invoice_open_date_begin'] = self.invoice_open_date_begin.to_alipay_dict()
            else:
                params['invoice_open_date_begin'] = self.invoice_open_date_begin
        if self.invoice_open_date_end:
            if hasattr(self.invoice_open_date_end, 'to_alipay_dict'):
                params['invoice_open_date_end'] = self.invoice_open_date_end.to_alipay_dict()
            else:
                params['invoice_open_date_end'] = self.invoice_open_date_end
        if self.invoice_types:
            if isinstance(self.invoice_types, list):
                for i in range(0, len(self.invoice_types)):
                    element = self.invoice_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_types[i] = element.to_alipay_dict()
            if hasattr(self.invoice_types, 'to_alipay_dict'):
                params['invoice_types'] = self.invoice_types.to_alipay_dict()
            else:
                params['invoice_types'] = self.invoice_types
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.order_nos:
            if isinstance(self.order_nos, list):
                for i in range(0, len(self.order_nos)):
                    element = self.order_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_nos[i] = element.to_alipay_dict()
            if hasattr(self.order_nos, 'to_alipay_dict'):
                params['order_nos'] = self.order_nos.to_alipay_dict()
            else:
                params['order_nos'] = self.order_nos
        if self.order_status:
            if isinstance(self.order_status, list):
                for i in range(0, len(self.order_status)):
                    element = self.order_status[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_status[i] = element.to_alipay_dict()
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.return_reason_types:
            if isinstance(self.return_reason_types, list):
                for i in range(0, len(self.return_reason_types)):
                    element = self.return_reason_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.return_reason_types[i] = element.to_alipay_dict()
            if hasattr(self.return_reason_types, 'to_alipay_dict'):
                params['return_reason_types'] = self.return_reason_types.to_alipay_dict()
            else:
                params['return_reason_types'] = self.return_reason_types
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.tracking_no:
            if hasattr(self.tracking_no, 'to_alipay_dict'):
                params['tracking_no'] = self.tracking_no.to_alipay_dict()
            else:
                params['tracking_no'] = self.tracking_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncInvoiceReturnorderBatchqueryModel()
        if 'apply_date_begin' in d:
            o.apply_date_begin = d['apply_date_begin']
        if 'apply_date_end' in d:
            o.apply_date_end = d['apply_date_end']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_open_date_begin' in d:
            o.invoice_open_date_begin = d['invoice_open_date_begin']
        if 'invoice_open_date_end' in d:
            o.invoice_open_date_end = d['invoice_open_date_end']
        if 'invoice_types' in d:
            o.invoice_types = d['invoice_types']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'order_nos' in d:
            o.order_nos = d['order_nos']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'return_reason_types' in d:
            o.return_reason_types = d['return_reason_types']
        if 'source' in d:
            o.source = d['source']
        if 'tracking_no' in d:
            o.tracking_no = d['tracking_no']
        return o



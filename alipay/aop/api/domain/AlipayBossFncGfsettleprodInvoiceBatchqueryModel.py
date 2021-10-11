#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncGfsettleprodInvoiceBatchqueryModel(object):

    def __init__(self):
        self._buyer_inst_id_list = None
        self._invoice_auth_date_begin = None
        self._invoice_auth_date_end = None
        self._invoice_code = None
        self._invoice_date_begin = None
        self._invoice_date_end = None
        self._invoice_id_list = None
        self._invoice_input_date_begin = None
        self._invoice_input_date_end = None
        self._invoice_no = None
        self._invoice_receive_date_begin = None
        self._invoice_receive_date_end = None
        self._invoice_status_list = None
        self._invoice_type_list = None
        self._kp_no = None
        self._page_num = None
        self._page_size = None
        self._seller_ip_role_ids = None

    @property
    def buyer_inst_id_list(self):
        return self._buyer_inst_id_list

    @buyer_inst_id_list.setter
    def buyer_inst_id_list(self, value):
        if isinstance(value, list):
            self._buyer_inst_id_list = list()
            for i in value:
                self._buyer_inst_id_list.append(i)
    @property
    def invoice_auth_date_begin(self):
        return self._invoice_auth_date_begin

    @invoice_auth_date_begin.setter
    def invoice_auth_date_begin(self, value):
        self._invoice_auth_date_begin = value
    @property
    def invoice_auth_date_end(self):
        return self._invoice_auth_date_end

    @invoice_auth_date_end.setter
    def invoice_auth_date_end(self, value):
        self._invoice_auth_date_end = value
    @property
    def invoice_code(self):
        return self._invoice_code

    @invoice_code.setter
    def invoice_code(self, value):
        self._invoice_code = value
    @property
    def invoice_date_begin(self):
        return self._invoice_date_begin

    @invoice_date_begin.setter
    def invoice_date_begin(self, value):
        self._invoice_date_begin = value
    @property
    def invoice_date_end(self):
        return self._invoice_date_end

    @invoice_date_end.setter
    def invoice_date_end(self, value):
        self._invoice_date_end = value
    @property
    def invoice_id_list(self):
        return self._invoice_id_list

    @invoice_id_list.setter
    def invoice_id_list(self, value):
        if isinstance(value, list):
            self._invoice_id_list = list()
            for i in value:
                self._invoice_id_list.append(i)
    @property
    def invoice_input_date_begin(self):
        return self._invoice_input_date_begin

    @invoice_input_date_begin.setter
    def invoice_input_date_begin(self, value):
        self._invoice_input_date_begin = value
    @property
    def invoice_input_date_end(self):
        return self._invoice_input_date_end

    @invoice_input_date_end.setter
    def invoice_input_date_end(self, value):
        self._invoice_input_date_end = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_receive_date_begin(self):
        return self._invoice_receive_date_begin

    @invoice_receive_date_begin.setter
    def invoice_receive_date_begin(self, value):
        self._invoice_receive_date_begin = value
    @property
    def invoice_receive_date_end(self):
        return self._invoice_receive_date_end

    @invoice_receive_date_end.setter
    def invoice_receive_date_end(self, value):
        self._invoice_receive_date_end = value
    @property
    def invoice_status_list(self):
        return self._invoice_status_list

    @invoice_status_list.setter
    def invoice_status_list(self, value):
        self._invoice_status_list = value
    @property
    def invoice_type_list(self):
        return self._invoice_type_list

    @invoice_type_list.setter
    def invoice_type_list(self, value):
        self._invoice_type_list = value
    @property
    def kp_no(self):
        return self._kp_no

    @kp_no.setter
    def kp_no(self, value):
        self._kp_no = value
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
    def seller_ip_role_ids(self):
        return self._seller_ip_role_ids

    @seller_ip_role_ids.setter
    def seller_ip_role_ids(self, value):
        if isinstance(value, list):
            self._seller_ip_role_ids = list()
            for i in value:
                self._seller_ip_role_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_inst_id_list:
            if isinstance(self.buyer_inst_id_list, list):
                for i in range(0, len(self.buyer_inst_id_list)):
                    element = self.buyer_inst_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.buyer_inst_id_list[i] = element.to_alipay_dict()
            if hasattr(self.buyer_inst_id_list, 'to_alipay_dict'):
                params['buyer_inst_id_list'] = self.buyer_inst_id_list.to_alipay_dict()
            else:
                params['buyer_inst_id_list'] = self.buyer_inst_id_list
        if self.invoice_auth_date_begin:
            if hasattr(self.invoice_auth_date_begin, 'to_alipay_dict'):
                params['invoice_auth_date_begin'] = self.invoice_auth_date_begin.to_alipay_dict()
            else:
                params['invoice_auth_date_begin'] = self.invoice_auth_date_begin
        if self.invoice_auth_date_end:
            if hasattr(self.invoice_auth_date_end, 'to_alipay_dict'):
                params['invoice_auth_date_end'] = self.invoice_auth_date_end.to_alipay_dict()
            else:
                params['invoice_auth_date_end'] = self.invoice_auth_date_end
        if self.invoice_code:
            if hasattr(self.invoice_code, 'to_alipay_dict'):
                params['invoice_code'] = self.invoice_code.to_alipay_dict()
            else:
                params['invoice_code'] = self.invoice_code
        if self.invoice_date_begin:
            if hasattr(self.invoice_date_begin, 'to_alipay_dict'):
                params['invoice_date_begin'] = self.invoice_date_begin.to_alipay_dict()
            else:
                params['invoice_date_begin'] = self.invoice_date_begin
        if self.invoice_date_end:
            if hasattr(self.invoice_date_end, 'to_alipay_dict'):
                params['invoice_date_end'] = self.invoice_date_end.to_alipay_dict()
            else:
                params['invoice_date_end'] = self.invoice_date_end
        if self.invoice_id_list:
            if isinstance(self.invoice_id_list, list):
                for i in range(0, len(self.invoice_id_list)):
                    element = self.invoice_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_id_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_id_list, 'to_alipay_dict'):
                params['invoice_id_list'] = self.invoice_id_list.to_alipay_dict()
            else:
                params['invoice_id_list'] = self.invoice_id_list
        if self.invoice_input_date_begin:
            if hasattr(self.invoice_input_date_begin, 'to_alipay_dict'):
                params['invoice_input_date_begin'] = self.invoice_input_date_begin.to_alipay_dict()
            else:
                params['invoice_input_date_begin'] = self.invoice_input_date_begin
        if self.invoice_input_date_end:
            if hasattr(self.invoice_input_date_end, 'to_alipay_dict'):
                params['invoice_input_date_end'] = self.invoice_input_date_end.to_alipay_dict()
            else:
                params['invoice_input_date_end'] = self.invoice_input_date_end
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_receive_date_begin:
            if hasattr(self.invoice_receive_date_begin, 'to_alipay_dict'):
                params['invoice_receive_date_begin'] = self.invoice_receive_date_begin.to_alipay_dict()
            else:
                params['invoice_receive_date_begin'] = self.invoice_receive_date_begin
        if self.invoice_receive_date_end:
            if hasattr(self.invoice_receive_date_end, 'to_alipay_dict'):
                params['invoice_receive_date_end'] = self.invoice_receive_date_end.to_alipay_dict()
            else:
                params['invoice_receive_date_end'] = self.invoice_receive_date_end
        if self.invoice_status_list:
            if hasattr(self.invoice_status_list, 'to_alipay_dict'):
                params['invoice_status_list'] = self.invoice_status_list.to_alipay_dict()
            else:
                params['invoice_status_list'] = self.invoice_status_list
        if self.invoice_type_list:
            if hasattr(self.invoice_type_list, 'to_alipay_dict'):
                params['invoice_type_list'] = self.invoice_type_list.to_alipay_dict()
            else:
                params['invoice_type_list'] = self.invoice_type_list
        if self.kp_no:
            if hasattr(self.kp_no, 'to_alipay_dict'):
                params['kp_no'] = self.kp_no.to_alipay_dict()
            else:
                params['kp_no'] = self.kp_no
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
        if self.seller_ip_role_ids:
            if isinstance(self.seller_ip_role_ids, list):
                for i in range(0, len(self.seller_ip_role_ids)):
                    element = self.seller_ip_role_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.seller_ip_role_ids[i] = element.to_alipay_dict()
            if hasattr(self.seller_ip_role_ids, 'to_alipay_dict'):
                params['seller_ip_role_ids'] = self.seller_ip_role_ids.to_alipay_dict()
            else:
                params['seller_ip_role_ids'] = self.seller_ip_role_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodInvoiceBatchqueryModel()
        if 'buyer_inst_id_list' in d:
            o.buyer_inst_id_list = d['buyer_inst_id_list']
        if 'invoice_auth_date_begin' in d:
            o.invoice_auth_date_begin = d['invoice_auth_date_begin']
        if 'invoice_auth_date_end' in d:
            o.invoice_auth_date_end = d['invoice_auth_date_end']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date_begin' in d:
            o.invoice_date_begin = d['invoice_date_begin']
        if 'invoice_date_end' in d:
            o.invoice_date_end = d['invoice_date_end']
        if 'invoice_id_list' in d:
            o.invoice_id_list = d['invoice_id_list']
        if 'invoice_input_date_begin' in d:
            o.invoice_input_date_begin = d['invoice_input_date_begin']
        if 'invoice_input_date_end' in d:
            o.invoice_input_date_end = d['invoice_input_date_end']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_receive_date_begin' in d:
            o.invoice_receive_date_begin = d['invoice_receive_date_begin']
        if 'invoice_receive_date_end' in d:
            o.invoice_receive_date_end = d['invoice_receive_date_end']
        if 'invoice_status_list' in d:
            o.invoice_status_list = d['invoice_status_list']
        if 'invoice_type_list' in d:
            o.invoice_type_list = d['invoice_type_list']
        if 'kp_no' in d:
            o.kp_no = d['kp_no']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'seller_ip_role_ids' in d:
            o.seller_ip_role_ids = d['seller_ip_role_ids']
        return o



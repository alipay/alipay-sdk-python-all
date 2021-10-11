#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CollectReceiptQueryOpenApiOrder(object):

    def __init__(self):
        self._ccy = None
        self._channel_list = None
        self._channel_log_no = None
        self._collect_end_date = None
        self._collect_start_date = None
        self._inst_id_list = None
        self._page_num = None
        self._page_size = None
        self._payee_account_no = None
        self._payer_account_no = None
        self._payer_ip_role_id = None
        self._receipt_no = None
        self._source_list = None
        self._status_list = None

    @property
    def ccy(self):
        return self._ccy

    @ccy.setter
    def ccy(self, value):
        self._ccy = value
    @property
    def channel_list(self):
        return self._channel_list

    @channel_list.setter
    def channel_list(self, value):
        if isinstance(value, list):
            self._channel_list = list()
            for i in value:
                self._channel_list.append(i)
    @property
    def channel_log_no(self):
        return self._channel_log_no

    @channel_log_no.setter
    def channel_log_no(self, value):
        self._channel_log_no = value
    @property
    def collect_end_date(self):
        return self._collect_end_date

    @collect_end_date.setter
    def collect_end_date(self, value):
        self._collect_end_date = value
    @property
    def collect_start_date(self):
        return self._collect_start_date

    @collect_start_date.setter
    def collect_start_date(self, value):
        self._collect_start_date = value
    @property
    def inst_id_list(self):
        return self._inst_id_list

    @inst_id_list.setter
    def inst_id_list(self, value):
        if isinstance(value, list):
            self._inst_id_list = list()
            for i in value:
                self._inst_id_list.append(i)
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
    def payee_account_no(self):
        return self._payee_account_no

    @payee_account_no.setter
    def payee_account_no(self, value):
        self._payee_account_no = value
    @property
    def payer_account_no(self):
        return self._payer_account_no

    @payer_account_no.setter
    def payer_account_no(self, value):
        self._payer_account_no = value
    @property
    def payer_ip_role_id(self):
        return self._payer_ip_role_id

    @payer_ip_role_id.setter
    def payer_ip_role_id(self, value):
        self._payer_ip_role_id = value
    @property
    def receipt_no(self):
        return self._receipt_no

    @receipt_no.setter
    def receipt_no(self, value):
        self._receipt_no = value
    @property
    def source_list(self):
        return self._source_list

    @source_list.setter
    def source_list(self, value):
        if isinstance(value, list):
            self._source_list = list()
            for i in value:
                self._source_list.append(i)
    @property
    def status_list(self):
        return self._status_list

    @status_list.setter
    def status_list(self, value):
        if isinstance(value, list):
            self._status_list = list()
            for i in value:
                self._status_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.ccy:
            if hasattr(self.ccy, 'to_alipay_dict'):
                params['ccy'] = self.ccy.to_alipay_dict()
            else:
                params['ccy'] = self.ccy
        if self.channel_list:
            if isinstance(self.channel_list, list):
                for i in range(0, len(self.channel_list)):
                    element = self.channel_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.channel_list[i] = element.to_alipay_dict()
            if hasattr(self.channel_list, 'to_alipay_dict'):
                params['channel_list'] = self.channel_list.to_alipay_dict()
            else:
                params['channel_list'] = self.channel_list
        if self.channel_log_no:
            if hasattr(self.channel_log_no, 'to_alipay_dict'):
                params['channel_log_no'] = self.channel_log_no.to_alipay_dict()
            else:
                params['channel_log_no'] = self.channel_log_no
        if self.collect_end_date:
            if hasattr(self.collect_end_date, 'to_alipay_dict'):
                params['collect_end_date'] = self.collect_end_date.to_alipay_dict()
            else:
                params['collect_end_date'] = self.collect_end_date
        if self.collect_start_date:
            if hasattr(self.collect_start_date, 'to_alipay_dict'):
                params['collect_start_date'] = self.collect_start_date.to_alipay_dict()
            else:
                params['collect_start_date'] = self.collect_start_date
        if self.inst_id_list:
            if isinstance(self.inst_id_list, list):
                for i in range(0, len(self.inst_id_list)):
                    element = self.inst_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inst_id_list[i] = element.to_alipay_dict()
            if hasattr(self.inst_id_list, 'to_alipay_dict'):
                params['inst_id_list'] = self.inst_id_list.to_alipay_dict()
            else:
                params['inst_id_list'] = self.inst_id_list
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
        if self.payee_account_no:
            if hasattr(self.payee_account_no, 'to_alipay_dict'):
                params['payee_account_no'] = self.payee_account_no.to_alipay_dict()
            else:
                params['payee_account_no'] = self.payee_account_no
        if self.payer_account_no:
            if hasattr(self.payer_account_no, 'to_alipay_dict'):
                params['payer_account_no'] = self.payer_account_no.to_alipay_dict()
            else:
                params['payer_account_no'] = self.payer_account_no
        if self.payer_ip_role_id:
            if hasattr(self.payer_ip_role_id, 'to_alipay_dict'):
                params['payer_ip_role_id'] = self.payer_ip_role_id.to_alipay_dict()
            else:
                params['payer_ip_role_id'] = self.payer_ip_role_id
        if self.receipt_no:
            if hasattr(self.receipt_no, 'to_alipay_dict'):
                params['receipt_no'] = self.receipt_no.to_alipay_dict()
            else:
                params['receipt_no'] = self.receipt_no
        if self.source_list:
            if isinstance(self.source_list, list):
                for i in range(0, len(self.source_list)):
                    element = self.source_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.source_list[i] = element.to_alipay_dict()
            if hasattr(self.source_list, 'to_alipay_dict'):
                params['source_list'] = self.source_list.to_alipay_dict()
            else:
                params['source_list'] = self.source_list
        if self.status_list:
            if isinstance(self.status_list, list):
                for i in range(0, len(self.status_list)):
                    element = self.status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.status_list[i] = element.to_alipay_dict()
            if hasattr(self.status_list, 'to_alipay_dict'):
                params['status_list'] = self.status_list.to_alipay_dict()
            else:
                params['status_list'] = self.status_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CollectReceiptQueryOpenApiOrder()
        if 'ccy' in d:
            o.ccy = d['ccy']
        if 'channel_list' in d:
            o.channel_list = d['channel_list']
        if 'channel_log_no' in d:
            o.channel_log_no = d['channel_log_no']
        if 'collect_end_date' in d:
            o.collect_end_date = d['collect_end_date']
        if 'collect_start_date' in d:
            o.collect_start_date = d['collect_start_date']
        if 'inst_id_list' in d:
            o.inst_id_list = d['inst_id_list']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'payee_account_no' in d:
            o.payee_account_no = d['payee_account_no']
        if 'payer_account_no' in d:
            o.payer_account_no = d['payer_account_no']
        if 'payer_ip_role_id' in d:
            o.payer_ip_role_id = d['payer_ip_role_id']
        if 'receipt_no' in d:
            o.receipt_no = d['receipt_no']
        if 'source_list' in d:
            o.source_list = d['source_list']
        if 'status_list' in d:
            o.status_list = d['status_list']
        return o



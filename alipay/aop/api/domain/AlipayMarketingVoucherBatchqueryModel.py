#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VcpUniqueInfo import VcpUniqueInfo


class AlipayMarketingVoucherBatchqueryModel(object):

    def __init__(self):
        self._biz_codes = None
        self._create_end_time = None
        self._create_start_time = None
        self._freeze_codes = None
        self._page_num = None
        self._page_size = None
        self._product_codes = None
        self._sort_type = None
        self._status_list = None
        self._template_extend_info = None
        self._template_ids = None
        self._user_info = None
        self._voucher_extend_info = None

    @property
    def biz_codes(self):
        return self._biz_codes

    @biz_codes.setter
    def biz_codes(self, value):
        if isinstance(value, list):
            self._biz_codes = list()
            for i in value:
                self._biz_codes.append(i)
    @property
    def create_end_time(self):
        return self._create_end_time

    @create_end_time.setter
    def create_end_time(self, value):
        self._create_end_time = value
    @property
    def create_start_time(self):
        return self._create_start_time

    @create_start_time.setter
    def create_start_time(self, value):
        self._create_start_time = value
    @property
    def freeze_codes(self):
        return self._freeze_codes

    @freeze_codes.setter
    def freeze_codes(self, value):
        if isinstance(value, list):
            self._freeze_codes = list()
            for i in value:
                self._freeze_codes.append(i)
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
    def product_codes(self):
        return self._product_codes

    @product_codes.setter
    def product_codes(self, value):
        if isinstance(value, list):
            self._product_codes = list()
            for i in value:
                self._product_codes.append(i)
    @property
    def sort_type(self):
        return self._sort_type

    @sort_type.setter
    def sort_type(self, value):
        self._sort_type = value
    @property
    def status_list(self):
        return self._status_list

    @status_list.setter
    def status_list(self, value):
        if isinstance(value, list):
            self._status_list = list()
            for i in value:
                self._status_list.append(i)
    @property
    def template_extend_info(self):
        return self._template_extend_info

    @template_extend_info.setter
    def template_extend_info(self, value):
        self._template_extend_info = value
    @property
    def template_ids(self):
        return self._template_ids

    @template_ids.setter
    def template_ids(self, value):
        if isinstance(value, list):
            self._template_ids = list()
            for i in value:
                self._template_ids.append(i)
    @property
    def user_info(self):
        return self._user_info

    @user_info.setter
    def user_info(self, value):
        if isinstance(value, VcpUniqueInfo):
            self._user_info = value
        else:
            self._user_info = VcpUniqueInfo.from_alipay_dict(value)
    @property
    def voucher_extend_info(self):
        return self._voucher_extend_info

    @voucher_extend_info.setter
    def voucher_extend_info(self, value):
        self._voucher_extend_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_codes:
            if isinstance(self.biz_codes, list):
                for i in range(0, len(self.biz_codes)):
                    element = self.biz_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_codes[i] = element.to_alipay_dict()
            if hasattr(self.biz_codes, 'to_alipay_dict'):
                params['biz_codes'] = self.biz_codes.to_alipay_dict()
            else:
                params['biz_codes'] = self.biz_codes
        if self.create_end_time:
            if hasattr(self.create_end_time, 'to_alipay_dict'):
                params['create_end_time'] = self.create_end_time.to_alipay_dict()
            else:
                params['create_end_time'] = self.create_end_time
        if self.create_start_time:
            if hasattr(self.create_start_time, 'to_alipay_dict'):
                params['create_start_time'] = self.create_start_time.to_alipay_dict()
            else:
                params['create_start_time'] = self.create_start_time
        if self.freeze_codes:
            if isinstance(self.freeze_codes, list):
                for i in range(0, len(self.freeze_codes)):
                    element = self.freeze_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.freeze_codes[i] = element.to_alipay_dict()
            if hasattr(self.freeze_codes, 'to_alipay_dict'):
                params['freeze_codes'] = self.freeze_codes.to_alipay_dict()
            else:
                params['freeze_codes'] = self.freeze_codes
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
        if self.product_codes:
            if isinstance(self.product_codes, list):
                for i in range(0, len(self.product_codes)):
                    element = self.product_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_codes[i] = element.to_alipay_dict()
            if hasattr(self.product_codes, 'to_alipay_dict'):
                params['product_codes'] = self.product_codes.to_alipay_dict()
            else:
                params['product_codes'] = self.product_codes
        if self.sort_type:
            if hasattr(self.sort_type, 'to_alipay_dict'):
                params['sort_type'] = self.sort_type.to_alipay_dict()
            else:
                params['sort_type'] = self.sort_type
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
        if self.template_extend_info:
            if hasattr(self.template_extend_info, 'to_alipay_dict'):
                params['template_extend_info'] = self.template_extend_info.to_alipay_dict()
            else:
                params['template_extend_info'] = self.template_extend_info
        if self.template_ids:
            if isinstance(self.template_ids, list):
                for i in range(0, len(self.template_ids)):
                    element = self.template_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.template_ids[i] = element.to_alipay_dict()
            if hasattr(self.template_ids, 'to_alipay_dict'):
                params['template_ids'] = self.template_ids.to_alipay_dict()
            else:
                params['template_ids'] = self.template_ids
        if self.user_info:
            if hasattr(self.user_info, 'to_alipay_dict'):
                params['user_info'] = self.user_info.to_alipay_dict()
            else:
                params['user_info'] = self.user_info
        if self.voucher_extend_info:
            if hasattr(self.voucher_extend_info, 'to_alipay_dict'):
                params['voucher_extend_info'] = self.voucher_extend_info.to_alipay_dict()
            else:
                params['voucher_extend_info'] = self.voucher_extend_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingVoucherBatchqueryModel()
        if 'biz_codes' in d:
            o.biz_codes = d['biz_codes']
        if 'create_end_time' in d:
            o.create_end_time = d['create_end_time']
        if 'create_start_time' in d:
            o.create_start_time = d['create_start_time']
        if 'freeze_codes' in d:
            o.freeze_codes = d['freeze_codes']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'product_codes' in d:
            o.product_codes = d['product_codes']
        if 'sort_type' in d:
            o.sort_type = d['sort_type']
        if 'status_list' in d:
            o.status_list = d['status_list']
        if 'template_extend_info' in d:
            o.template_extend_info = d['template_extend_info']
        if 'template_ids' in d:
            o.template_ids = d['template_ids']
        if 'user_info' in d:
            o.user_info = d['user_info']
        if 'voucher_extend_info' in d:
            o.voucher_extend_info = d['voucher_extend_info']
        return o



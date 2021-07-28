#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerversionQueryModel(object):

    def __init__(self):
        self._bundle_id = None
        self._bundle_ids = None
        self._first_sort_col = None
        self._first_sort_col_order = None
        self._group_status_list = None
        self._inst_code = None
        self._mini_app_id = None
        self._mini_app_id_list = None
        self._page_num = None
        self._page_size = None
        self._version_list = None

    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def bundle_ids(self):
        return self._bundle_ids

    @bundle_ids.setter
    def bundle_ids(self, value):
        if isinstance(value, list):
            self._bundle_ids = list()
            for i in value:
                self._bundle_ids.append(i)
    @property
    def first_sort_col(self):
        return self._first_sort_col

    @first_sort_col.setter
    def first_sort_col(self, value):
        self._first_sort_col = value
    @property
    def first_sort_col_order(self):
        return self._first_sort_col_order

    @first_sort_col_order.setter
    def first_sort_col_order(self, value):
        self._first_sort_col_order = value
    @property
    def group_status_list(self):
        return self._group_status_list

    @group_status_list.setter
    def group_status_list(self, value):
        if isinstance(value, list):
            self._group_status_list = list()
            for i in value:
                self._group_status_list.append(i)
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def mini_app_id_list(self):
        return self._mini_app_id_list

    @mini_app_id_list.setter
    def mini_app_id_list(self, value):
        if isinstance(value, list):
            self._mini_app_id_list = list()
            for i in value:
                self._mini_app_id_list.append(i)
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
    def version_list(self):
        return self._version_list

    @version_list.setter
    def version_list(self, value):
        if isinstance(value, list):
            self._version_list = list()
            for i in value:
                self._version_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.bundle_ids:
            if isinstance(self.bundle_ids, list):
                for i in range(0, len(self.bundle_ids)):
                    element = self.bundle_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bundle_ids[i] = element.to_alipay_dict()
            if hasattr(self.bundle_ids, 'to_alipay_dict'):
                params['bundle_ids'] = self.bundle_ids.to_alipay_dict()
            else:
                params['bundle_ids'] = self.bundle_ids
        if self.first_sort_col:
            if hasattr(self.first_sort_col, 'to_alipay_dict'):
                params['first_sort_col'] = self.first_sort_col.to_alipay_dict()
            else:
                params['first_sort_col'] = self.first_sort_col
        if self.first_sort_col_order:
            if hasattr(self.first_sort_col_order, 'to_alipay_dict'):
                params['first_sort_col_order'] = self.first_sort_col_order.to_alipay_dict()
            else:
                params['first_sort_col_order'] = self.first_sort_col_order
        if self.group_status_list:
            if isinstance(self.group_status_list, list):
                for i in range(0, len(self.group_status_list)):
                    element = self.group_status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_status_list[i] = element.to_alipay_dict()
            if hasattr(self.group_status_list, 'to_alipay_dict'):
                params['group_status_list'] = self.group_status_list.to_alipay_dict()
            else:
                params['group_status_list'] = self.group_status_list
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.mini_app_id_list:
            if isinstance(self.mini_app_id_list, list):
                for i in range(0, len(self.mini_app_id_list)):
                    element = self.mini_app_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mini_app_id_list[i] = element.to_alipay_dict()
            if hasattr(self.mini_app_id_list, 'to_alipay_dict'):
                params['mini_app_id_list'] = self.mini_app_id_list.to_alipay_dict()
            else:
                params['mini_app_id_list'] = self.mini_app_id_list
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
        if self.version_list:
            if isinstance(self.version_list, list):
                for i in range(0, len(self.version_list)):
                    element = self.version_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.version_list[i] = element.to_alipay_dict()
            if hasattr(self.version_list, 'to_alipay_dict'):
                params['version_list'] = self.version_list.to_alipay_dict()
            else:
                params['version_list'] = self.version_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerversionQueryModel()
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'bundle_ids' in d:
            o.bundle_ids = d['bundle_ids']
        if 'first_sort_col' in d:
            o.first_sort_col = d['first_sort_col']
        if 'first_sort_col_order' in d:
            o.first_sort_col_order = d['first_sort_col_order']
        if 'group_status_list' in d:
            o.group_status_list = d['group_status_list']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'mini_app_id_list' in d:
            o.mini_app_id_list = d['mini_app_id_list']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'version_list' in d:
            o.version_list = d['version_list']
        return o



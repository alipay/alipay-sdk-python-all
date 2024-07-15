#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdCompanyauthQueryModel(object):

    def __init__(self):
        self._app_code = None
        self._company_id_list = None
        self._company_name = None
        self._company_name_fuzzy = None
        self._ou_code = None
        self._page_num = None
        self._page_size = None
        self._paging = None
        self._usage_scene = None

    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def company_id_list(self):
        return self._company_id_list

    @company_id_list.setter
    def company_id_list(self, value):
        self._company_id_list = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def company_name_fuzzy(self):
        return self._company_name_fuzzy

    @company_name_fuzzy.setter
    def company_name_fuzzy(self, value):
        self._company_name_fuzzy = value
    @property
    def ou_code(self):
        return self._ou_code

    @ou_code.setter
    def ou_code(self, value):
        self._ou_code = value
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
    def paging(self):
        return self._paging

    @paging.setter
    def paging(self, value):
        self._paging = value
    @property
    def usage_scene(self):
        return self._usage_scene

    @usage_scene.setter
    def usage_scene(self, value):
        self._usage_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.company_id_list:
            if hasattr(self.company_id_list, 'to_alipay_dict'):
                params['company_id_list'] = self.company_id_list.to_alipay_dict()
            else:
                params['company_id_list'] = self.company_id_list
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.company_name_fuzzy:
            if hasattr(self.company_name_fuzzy, 'to_alipay_dict'):
                params['company_name_fuzzy'] = self.company_name_fuzzy.to_alipay_dict()
            else:
                params['company_name_fuzzy'] = self.company_name_fuzzy
        if self.ou_code:
            if hasattr(self.ou_code, 'to_alipay_dict'):
                params['ou_code'] = self.ou_code.to_alipay_dict()
            else:
                params['ou_code'] = self.ou_code
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
        if self.paging:
            if hasattr(self.paging, 'to_alipay_dict'):
                params['paging'] = self.paging.to_alipay_dict()
            else:
                params['paging'] = self.paging
        if self.usage_scene:
            if hasattr(self.usage_scene, 'to_alipay_dict'):
                params['usage_scene'] = self.usage_scene.to_alipay_dict()
            else:
                params['usage_scene'] = self.usage_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdCompanyauthQueryModel()
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'company_id_list' in d:
            o.company_id_list = d['company_id_list']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'company_name_fuzzy' in d:
            o.company_name_fuzzy = d['company_name_fuzzy']
        if 'ou_code' in d:
            o.ou_code = d['ou_code']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'paging' in d:
            o.paging = d['paging']
        if 'usage_scene' in d:
            o.usage_scene = d['usage_scene']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OfferObject(object):

    def __init__(self):
        self._app_code = None
        self._category_code = None
        self._city_code = None
        self._displayapp_id = None
        self._displayapp_memo = None
        self._displayapp_name = None
        self._displayapp_status = None
        self._displayapp_url = None
        self._gmt_create = None
        self._gmt_modified = None
        self._logo_url = None
        self._service_url = None

    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def displayapp_id(self):
        return self._displayapp_id

    @displayapp_id.setter
    def displayapp_id(self, value):
        self._displayapp_id = value
    @property
    def displayapp_memo(self):
        return self._displayapp_memo

    @displayapp_memo.setter
    def displayapp_memo(self, value):
        self._displayapp_memo = value
    @property
    def displayapp_name(self):
        return self._displayapp_name

    @displayapp_name.setter
    def displayapp_name(self, value):
        self._displayapp_name = value
    @property
    def displayapp_status(self):
        return self._displayapp_status

    @displayapp_status.setter
    def displayapp_status(self, value):
        self._displayapp_status = value
    @property
    def displayapp_url(self):
        return self._displayapp_url

    @displayapp_url.setter
    def displayapp_url(self, value):
        self._displayapp_url = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def service_url(self):
        return self._service_url

    @service_url.setter
    def service_url(self, value):
        self._service_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.displayapp_id:
            if hasattr(self.displayapp_id, 'to_alipay_dict'):
                params['displayapp_id'] = self.displayapp_id.to_alipay_dict()
            else:
                params['displayapp_id'] = self.displayapp_id
        if self.displayapp_memo:
            if hasattr(self.displayapp_memo, 'to_alipay_dict'):
                params['displayapp_memo'] = self.displayapp_memo.to_alipay_dict()
            else:
                params['displayapp_memo'] = self.displayapp_memo
        if self.displayapp_name:
            if hasattr(self.displayapp_name, 'to_alipay_dict'):
                params['displayapp_name'] = self.displayapp_name.to_alipay_dict()
            else:
                params['displayapp_name'] = self.displayapp_name
        if self.displayapp_status:
            if hasattr(self.displayapp_status, 'to_alipay_dict'):
                params['displayapp_status'] = self.displayapp_status.to_alipay_dict()
            else:
                params['displayapp_status'] = self.displayapp_status
        if self.displayapp_url:
            if hasattr(self.displayapp_url, 'to_alipay_dict'):
                params['displayapp_url'] = self.displayapp_url.to_alipay_dict()
            else:
                params['displayapp_url'] = self.displayapp_url
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        if self.service_url:
            if hasattr(self.service_url, 'to_alipay_dict'):
                params['service_url'] = self.service_url.to_alipay_dict()
            else:
                params['service_url'] = self.service_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OfferObject()
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'displayapp_id' in d:
            o.displayapp_id = d['displayapp_id']
        if 'displayapp_memo' in d:
            o.displayapp_memo = d['displayapp_memo']
        if 'displayapp_name' in d:
            o.displayapp_name = d['displayapp_name']
        if 'displayapp_status' in d:
            o.displayapp_status = d['displayapp_status']
        if 'displayapp_url' in d:
            o.displayapp_url = d['displayapp_url']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'service_url' in d:
            o.service_url = d['service_url']
        return o



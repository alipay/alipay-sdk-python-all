#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommodityPublicExtInfos(object):

    def __init__(self):
        self._action_url = None
        self._app_id = None
        self._category_name = None
        self._city_name = None
        self._commodity_id = None
        self._create_user_id = None
        self._displayapp_id = None
        self._displayapp_memo = None
        self._displayapp_name = None
        self._displayapp_status = None
        self._displayapp_url = None
        self._export_url = None
        self._property_id = None

    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value
    @property
    def app_id(self):
        return self._app_id

    @app_id.setter
    def app_id(self, value):
        self._app_id = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def commodity_id(self):
        return self._commodity_id

    @commodity_id.setter
    def commodity_id(self, value):
        self._commodity_id = value
    @property
    def create_user_id(self):
        return self._create_user_id

    @create_user_id.setter
    def create_user_id(self, value):
        self._create_user_id = value
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
    def export_url(self):
        return self._export_url

    @export_url.setter
    def export_url(self, value):
        self._export_url = value
    @property
    def property_id(self):
        return self._property_id

    @property_id.setter
    def property_id(self, value):
        self._property_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_url:
            if hasattr(self.action_url, 'to_alipay_dict'):
                params['action_url'] = self.action_url.to_alipay_dict()
            else:
                params['action_url'] = self.action_url
        if self.app_id:
            if hasattr(self.app_id, 'to_alipay_dict'):
                params['app_id'] = self.app_id.to_alipay_dict()
            else:
                params['app_id'] = self.app_id
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.commodity_id:
            if hasattr(self.commodity_id, 'to_alipay_dict'):
                params['commodity_id'] = self.commodity_id.to_alipay_dict()
            else:
                params['commodity_id'] = self.commodity_id
        if self.create_user_id:
            if hasattr(self.create_user_id, 'to_alipay_dict'):
                params['create_user_id'] = self.create_user_id.to_alipay_dict()
            else:
                params['create_user_id'] = self.create_user_id
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
        if self.export_url:
            if hasattr(self.export_url, 'to_alipay_dict'):
                params['export_url'] = self.export_url.to_alipay_dict()
            else:
                params['export_url'] = self.export_url
        if self.property_id:
            if hasattr(self.property_id, 'to_alipay_dict'):
                params['property_id'] = self.property_id.to_alipay_dict()
            else:
                params['property_id'] = self.property_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommodityPublicExtInfos()
        if 'action_url' in d:
            o.action_url = d['action_url']
        if 'app_id' in d:
            o.app_id = d['app_id']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'commodity_id' in d:
            o.commodity_id = d['commodity_id']
        if 'create_user_id' in d:
            o.create_user_id = d['create_user_id']
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
        if 'export_url' in d:
            o.export_url = d['export_url']
        if 'property_id' in d:
            o.property_id = d['property_id']
        return o



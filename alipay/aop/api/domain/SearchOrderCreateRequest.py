#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SearchBaseItems import SearchBaseItems
from alipay.aop.api.domain.SearchBrandItems import SearchBrandItems
from alipay.aop.api.domain.SearchServiceItems import SearchServiceItems


class SearchOrderCreateRequest(object):

    def __init__(self):
        self._access_mode = None
        self._access_type = None
        self._action = None
        self._app_name = None
        self._appid = None
        self._base_items = None
        self._biz_id = None
        self._brand_down_grade = None
        self._brand_items = None
        self._create_type = None
        self._data_key = None
        self._descprise = None
        self._is_draft = None
        self._key_words = None
        self._online_time = None
        self._order_id = None
        self._ref_apply_id = None
        self._scene = None
        self._scene_name = None
        self._service_code = None
        self._service_items = None
        self._spec_code = None
        self._sub_service_code = None
        self._template_id = None
        self._template_type = None

    @property
    def access_mode(self):
        return self._access_mode

    @access_mode.setter
    def access_mode(self, value):
        self._access_mode = value
    @property
    def access_type(self):
        return self._access_type

    @access_type.setter
    def access_type(self, value):
        self._access_type = value
    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def appid(self):
        return self._appid

    @appid.setter
    def appid(self, value):
        self._appid = value
    @property
    def base_items(self):
        return self._base_items

    @base_items.setter
    def base_items(self, value):
        if isinstance(value, SearchBaseItems):
            self._base_items = value
        else:
            self._base_items = SearchBaseItems.from_alipay_dict(value)
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def brand_down_grade(self):
        return self._brand_down_grade

    @brand_down_grade.setter
    def brand_down_grade(self, value):
        self._brand_down_grade = value
    @property
    def brand_items(self):
        return self._brand_items

    @brand_items.setter
    def brand_items(self, value):
        if isinstance(value, SearchBrandItems):
            self._brand_items = value
        else:
            self._brand_items = SearchBrandItems.from_alipay_dict(value)
    @property
    def create_type(self):
        return self._create_type

    @create_type.setter
    def create_type(self, value):
        self._create_type = value
    @property
    def data_key(self):
        return self._data_key

    @data_key.setter
    def data_key(self, value):
        self._data_key = value
    @property
    def descprise(self):
        return self._descprise

    @descprise.setter
    def descprise(self, value):
        self._descprise = value
    @property
    def is_draft(self):
        return self._is_draft

    @is_draft.setter
    def is_draft(self, value):
        self._is_draft = value
    @property
    def key_words(self):
        return self._key_words

    @key_words.setter
    def key_words(self, value):
        self._key_words = value
    @property
    def online_time(self):
        return self._online_time

    @online_time.setter
    def online_time(self, value):
        self._online_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def ref_apply_id(self):
        return self._ref_apply_id

    @ref_apply_id.setter
    def ref_apply_id(self, value):
        self._ref_apply_id = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def scene_name(self):
        return self._scene_name

    @scene_name.setter
    def scene_name(self, value):
        self._scene_name = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_items(self):
        return self._service_items

    @service_items.setter
    def service_items(self, value):
        if isinstance(value, SearchServiceItems):
            self._service_items = value
        else:
            self._service_items = SearchServiceItems.from_alipay_dict(value)
    @property
    def spec_code(self):
        return self._spec_code

    @spec_code.setter
    def spec_code(self, value):
        self._spec_code = value
    @property
    def sub_service_code(self):
        return self._sub_service_code

    @sub_service_code.setter
    def sub_service_code(self, value):
        self._sub_service_code = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_type(self):
        return self._template_type

    @template_type.setter
    def template_type(self, value):
        self._template_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_mode:
            if hasattr(self.access_mode, 'to_alipay_dict'):
                params['access_mode'] = self.access_mode.to_alipay_dict()
            else:
                params['access_mode'] = self.access_mode
        if self.access_type:
            if hasattr(self.access_type, 'to_alipay_dict'):
                params['access_type'] = self.access_type.to_alipay_dict()
            else:
                params['access_type'] = self.access_type
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.appid:
            if hasattr(self.appid, 'to_alipay_dict'):
                params['appid'] = self.appid.to_alipay_dict()
            else:
                params['appid'] = self.appid
        if self.base_items:
            if hasattr(self.base_items, 'to_alipay_dict'):
                params['base_items'] = self.base_items.to_alipay_dict()
            else:
                params['base_items'] = self.base_items
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.brand_down_grade:
            if hasattr(self.brand_down_grade, 'to_alipay_dict'):
                params['brand_down_grade'] = self.brand_down_grade.to_alipay_dict()
            else:
                params['brand_down_grade'] = self.brand_down_grade
        if self.brand_items:
            if hasattr(self.brand_items, 'to_alipay_dict'):
                params['brand_items'] = self.brand_items.to_alipay_dict()
            else:
                params['brand_items'] = self.brand_items
        if self.create_type:
            if hasattr(self.create_type, 'to_alipay_dict'):
                params['create_type'] = self.create_type.to_alipay_dict()
            else:
                params['create_type'] = self.create_type
        if self.data_key:
            if hasattr(self.data_key, 'to_alipay_dict'):
                params['data_key'] = self.data_key.to_alipay_dict()
            else:
                params['data_key'] = self.data_key
        if self.descprise:
            if hasattr(self.descprise, 'to_alipay_dict'):
                params['descprise'] = self.descprise.to_alipay_dict()
            else:
                params['descprise'] = self.descprise
        if self.is_draft:
            if hasattr(self.is_draft, 'to_alipay_dict'):
                params['is_draft'] = self.is_draft.to_alipay_dict()
            else:
                params['is_draft'] = self.is_draft
        if self.key_words:
            if hasattr(self.key_words, 'to_alipay_dict'):
                params['key_words'] = self.key_words.to_alipay_dict()
            else:
                params['key_words'] = self.key_words
        if self.online_time:
            if hasattr(self.online_time, 'to_alipay_dict'):
                params['online_time'] = self.online_time.to_alipay_dict()
            else:
                params['online_time'] = self.online_time
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.ref_apply_id:
            if hasattr(self.ref_apply_id, 'to_alipay_dict'):
                params['ref_apply_id'] = self.ref_apply_id.to_alipay_dict()
            else:
                params['ref_apply_id'] = self.ref_apply_id
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.scene_name:
            if hasattr(self.scene_name, 'to_alipay_dict'):
                params['scene_name'] = self.scene_name.to_alipay_dict()
            else:
                params['scene_name'] = self.scene_name
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.service_items:
            if hasattr(self.service_items, 'to_alipay_dict'):
                params['service_items'] = self.service_items.to_alipay_dict()
            else:
                params['service_items'] = self.service_items
        if self.spec_code:
            if hasattr(self.spec_code, 'to_alipay_dict'):
                params['spec_code'] = self.spec_code.to_alipay_dict()
            else:
                params['spec_code'] = self.spec_code
        if self.sub_service_code:
            if hasattr(self.sub_service_code, 'to_alipay_dict'):
                params['sub_service_code'] = self.sub_service_code.to_alipay_dict()
            else:
                params['sub_service_code'] = self.sub_service_code
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.template_type:
            if hasattr(self.template_type, 'to_alipay_dict'):
                params['template_type'] = self.template_type.to_alipay_dict()
            else:
                params['template_type'] = self.template_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchOrderCreateRequest()
        if 'access_mode' in d:
            o.access_mode = d['access_mode']
        if 'access_type' in d:
            o.access_type = d['access_type']
        if 'action' in d:
            o.action = d['action']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'appid' in d:
            o.appid = d['appid']
        if 'base_items' in d:
            o.base_items = d['base_items']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'brand_down_grade' in d:
            o.brand_down_grade = d['brand_down_grade']
        if 'brand_items' in d:
            o.brand_items = d['brand_items']
        if 'create_type' in d:
            o.create_type = d['create_type']
        if 'data_key' in d:
            o.data_key = d['data_key']
        if 'descprise' in d:
            o.descprise = d['descprise']
        if 'is_draft' in d:
            o.is_draft = d['is_draft']
        if 'key_words' in d:
            o.key_words = d['key_words']
        if 'online_time' in d:
            o.online_time = d['online_time']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'ref_apply_id' in d:
            o.ref_apply_id = d['ref_apply_id']
        if 'scene' in d:
            o.scene = d['scene']
        if 'scene_name' in d:
            o.scene_name = d['scene_name']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_items' in d:
            o.service_items = d['service_items']
        if 'spec_code' in d:
            o.spec_code = d['spec_code']
        if 'sub_service_code' in d:
            o.sub_service_code = d['sub_service_code']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_type' in d:
            o.template_type = d['template_type']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerappPluginservicePublishModel(object):

    def __init__(self):
        self._ability_type_list = None
        self._app_logo = None
        self._app_origin = None
        self._description = None
        self._detail_for_client = None
        self._detail_for_pc = None
        self._mini_app_id = None
        self._sell_crowd = None
        self._show_type = None
        self._title = None
        self._visit_url_for_pc = None

    @property
    def ability_type_list(self):
        return self._ability_type_list

    @ability_type_list.setter
    def ability_type_list(self, value):
        if isinstance(value, list):
            self._ability_type_list = list()
            for i in value:
                self._ability_type_list.append(i)
    @property
    def app_logo(self):
        return self._app_logo

    @app_logo.setter
    def app_logo(self, value):
        self._app_logo = value
    @property
    def app_origin(self):
        return self._app_origin

    @app_origin.setter
    def app_origin(self, value):
        self._app_origin = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def detail_for_client(self):
        return self._detail_for_client

    @detail_for_client.setter
    def detail_for_client(self, value):
        self._detail_for_client = value
    @property
    def detail_for_pc(self):
        return self._detail_for_pc

    @detail_for_pc.setter
    def detail_for_pc(self, value):
        self._detail_for_pc = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def sell_crowd(self):
        return self._sell_crowd

    @sell_crowd.setter
    def sell_crowd(self, value):
        self._sell_crowd = value
    @property
    def show_type(self):
        return self._show_type

    @show_type.setter
    def show_type(self, value):
        self._show_type = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def visit_url_for_pc(self):
        return self._visit_url_for_pc

    @visit_url_for_pc.setter
    def visit_url_for_pc(self, value):
        self._visit_url_for_pc = value


    def to_alipay_dict(self):
        params = dict()
        if self.ability_type_list:
            if isinstance(self.ability_type_list, list):
                for i in range(0, len(self.ability_type_list)):
                    element = self.ability_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ability_type_list[i] = element.to_alipay_dict()
            if hasattr(self.ability_type_list, 'to_alipay_dict'):
                params['ability_type_list'] = self.ability_type_list.to_alipay_dict()
            else:
                params['ability_type_list'] = self.ability_type_list
        if self.app_logo:
            if hasattr(self.app_logo, 'to_alipay_dict'):
                params['app_logo'] = self.app_logo.to_alipay_dict()
            else:
                params['app_logo'] = self.app_logo
        if self.app_origin:
            if hasattr(self.app_origin, 'to_alipay_dict'):
                params['app_origin'] = self.app_origin.to_alipay_dict()
            else:
                params['app_origin'] = self.app_origin
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.detail_for_client:
            if hasattr(self.detail_for_client, 'to_alipay_dict'):
                params['detail_for_client'] = self.detail_for_client.to_alipay_dict()
            else:
                params['detail_for_client'] = self.detail_for_client
        if self.detail_for_pc:
            if hasattr(self.detail_for_pc, 'to_alipay_dict'):
                params['detail_for_pc'] = self.detail_for_pc.to_alipay_dict()
            else:
                params['detail_for_pc'] = self.detail_for_pc
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.sell_crowd:
            if hasattr(self.sell_crowd, 'to_alipay_dict'):
                params['sell_crowd'] = self.sell_crowd.to_alipay_dict()
            else:
                params['sell_crowd'] = self.sell_crowd
        if self.show_type:
            if hasattr(self.show_type, 'to_alipay_dict'):
                params['show_type'] = self.show_type.to_alipay_dict()
            else:
                params['show_type'] = self.show_type
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.visit_url_for_pc:
            if hasattr(self.visit_url_for_pc, 'to_alipay_dict'):
                params['visit_url_for_pc'] = self.visit_url_for_pc.to_alipay_dict()
            else:
                params['visit_url_for_pc'] = self.visit_url_for_pc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerappPluginservicePublishModel()
        if 'ability_type_list' in d:
            o.ability_type_list = d['ability_type_list']
        if 'app_logo' in d:
            o.app_logo = d['app_logo']
        if 'app_origin' in d:
            o.app_origin = d['app_origin']
        if 'description' in d:
            o.description = d['description']
        if 'detail_for_client' in d:
            o.detail_for_client = d['detail_for_client']
        if 'detail_for_pc' in d:
            o.detail_for_pc = d['detail_for_pc']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'sell_crowd' in d:
            o.sell_crowd = d['sell_crowd']
        if 'show_type' in d:
            o.show_type = d['show_type']
        if 'title' in d:
            o.title = d['title']
        if 'visit_url_for_pc' in d:
            o.visit_url_for_pc = d['visit_url_for_pc']
        return o



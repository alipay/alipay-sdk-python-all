#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ViewColumnInfoModel import ViewColumnInfoModel
from alipay.aop.api.domain.ViewStyleInfoModel import ViewStyleInfoModel


class MemberLevelModel(object):

    def __init__(self):
        self._code = None
        self._icon_img = None
        self._level = None
        self._name = None
        self._view_column_infos = None
        self._view_style_info = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def icon_img(self):
        return self._icon_img

    @icon_img.setter
    def icon_img(self, value):
        self._icon_img = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def view_column_infos(self):
        return self._view_column_infos

    @view_column_infos.setter
    def view_column_infos(self, value):
        if isinstance(value, list):
            self._view_column_infos = list()
            for i in value:
                if isinstance(i, ViewColumnInfoModel):
                    self._view_column_infos.append(i)
                else:
                    self._view_column_infos.append(ViewColumnInfoModel.from_alipay_dict(i))
    @property
    def view_style_info(self):
        return self._view_style_info

    @view_style_info.setter
    def view_style_info(self, value):
        if isinstance(value, ViewStyleInfoModel):
            self._view_style_info = value
        else:
            self._view_style_info = ViewStyleInfoModel.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.icon_img:
            if hasattr(self.icon_img, 'to_alipay_dict'):
                params['icon_img'] = self.icon_img.to_alipay_dict()
            else:
                params['icon_img'] = self.icon_img
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.view_column_infos:
            if isinstance(self.view_column_infos, list):
                for i in range(0, len(self.view_column_infos)):
                    element = self.view_column_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.view_column_infos[i] = element.to_alipay_dict()
            if hasattr(self.view_column_infos, 'to_alipay_dict'):
                params['view_column_infos'] = self.view_column_infos.to_alipay_dict()
            else:
                params['view_column_infos'] = self.view_column_infos
        if self.view_style_info:
            if hasattr(self.view_style_info, 'to_alipay_dict'):
                params['view_style_info'] = self.view_style_info.to_alipay_dict()
            else:
                params['view_style_info'] = self.view_style_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberLevelModel()
        if 'code' in d:
            o.code = d['code']
        if 'icon_img' in d:
            o.icon_img = d['icon_img']
        if 'level' in d:
            o.level = d['level']
        if 'name' in d:
            o.name = d['name']
        if 'view_column_infos' in d:
            o.view_column_infos = d['view_column_infos']
        if 'view_style_info' in d:
            o.view_style_info = d['view_style_info']
        return o



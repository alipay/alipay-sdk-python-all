#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankMarketingBkcustgrowprodCardstyleCreateModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._link_resource = None
        self._need_link = None
        self._selected = None
        self._source = None
        self._style_origin_id = None
        self._style_resource = None
        self._template_id = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def link_resource(self):
        return self._link_resource

    @link_resource.setter
    def link_resource(self, value):
        self._link_resource = value
    @property
    def need_link(self):
        return self._need_link

    @need_link.setter
    def need_link(self, value):
        self._need_link = value
    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, value):
        self._selected = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def style_origin_id(self):
        return self._style_origin_id

    @style_origin_id.setter
    def style_origin_id(self, value):
        self._style_origin_id = value
    @property
    def style_resource(self):
        return self._style_resource

    @style_resource.setter
    def style_resource(self, value):
        self._style_resource = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.link_resource:
            if hasattr(self.link_resource, 'to_alipay_dict'):
                params['link_resource'] = self.link_resource.to_alipay_dict()
            else:
                params['link_resource'] = self.link_resource
        if self.need_link:
            if hasattr(self.need_link, 'to_alipay_dict'):
                params['need_link'] = self.need_link.to_alipay_dict()
            else:
                params['need_link'] = self.need_link
        if self.selected:
            if hasattr(self.selected, 'to_alipay_dict'):
                params['selected'] = self.selected.to_alipay_dict()
            else:
                params['selected'] = self.selected
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.style_origin_id:
            if hasattr(self.style_origin_id, 'to_alipay_dict'):
                params['style_origin_id'] = self.style_origin_id.to_alipay_dict()
            else:
                params['style_origin_id'] = self.style_origin_id
        if self.style_resource:
            if hasattr(self.style_resource, 'to_alipay_dict'):
                params['style_resource'] = self.style_resource.to_alipay_dict()
            else:
                params['style_resource'] = self.style_resource
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankMarketingBkcustgrowprodCardstyleCreateModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'link_resource' in d:
            o.link_resource = d['link_resource']
        if 'need_link' in d:
            o.need_link = d['need_link']
        if 'selected' in d:
            o.selected = d['selected']
        if 'source' in d:
            o.source = d['source']
        if 'style_origin_id' in d:
            o.style_origin_id = d['style_origin_id']
        if 'style_resource' in d:
            o.style_resource = d['style_resource']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o



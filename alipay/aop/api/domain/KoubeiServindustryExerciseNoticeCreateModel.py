#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NoticeTemplateArgs import NoticeTemplateArgs


class KoubeiServindustryExerciseNoticeCreateModel(object):

    def __init__(self):
        self._external_notice_id = None
        self._fitness_id = None
        self._gmt_end = None
        self._gmt_start = None
        self._jump_url = None
        self._jump_url_type = None
        self._request_id = None
        self._shop_id = None
        self._sub_type = None
        self._template_args = None
        self._title = None
        self._type = None

    @property
    def external_notice_id(self):
        return self._external_notice_id

    @external_notice_id.setter
    def external_notice_id(self, value):
        self._external_notice_id = value
    @property
    def fitness_id(self):
        return self._fitness_id

    @fitness_id.setter
    def fitness_id(self, value):
        self._fitness_id = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def jump_url_type(self):
        return self._jump_url_type

    @jump_url_type.setter
    def jump_url_type(self, value):
        self._jump_url_type = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sub_type(self):
        return self._sub_type

    @sub_type.setter
    def sub_type(self, value):
        self._sub_type = value
    @property
    def template_args(self):
        return self._template_args

    @template_args.setter
    def template_args(self, value):
        if isinstance(value, NoticeTemplateArgs):
            self._template_args = value
        else:
            self._template_args = NoticeTemplateArgs.from_alipay_dict(value)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_notice_id:
            if hasattr(self.external_notice_id, 'to_alipay_dict'):
                params['external_notice_id'] = self.external_notice_id.to_alipay_dict()
            else:
                params['external_notice_id'] = self.external_notice_id
        if self.fitness_id:
            if hasattr(self.fitness_id, 'to_alipay_dict'):
                params['fitness_id'] = self.fitness_id.to_alipay_dict()
            else:
                params['fitness_id'] = self.fitness_id
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        if self.jump_url_type:
            if hasattr(self.jump_url_type, 'to_alipay_dict'):
                params['jump_url_type'] = self.jump_url_type.to_alipay_dict()
            else:
                params['jump_url_type'] = self.jump_url_type
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sub_type:
            if hasattr(self.sub_type, 'to_alipay_dict'):
                params['sub_type'] = self.sub_type.to_alipay_dict()
            else:
                params['sub_type'] = self.sub_type
        if self.template_args:
            if hasattr(self.template_args, 'to_alipay_dict'):
                params['template_args'] = self.template_args.to_alipay_dict()
            else:
                params['template_args'] = self.template_args
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiServindustryExerciseNoticeCreateModel()
        if 'external_notice_id' in d:
            o.external_notice_id = d['external_notice_id']
        if 'fitness_id' in d:
            o.fitness_id = d['fitness_id']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        if 'jump_url_type' in d:
            o.jump_url_type = d['jump_url_type']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sub_type' in d:
            o.sub_type = d['sub_type']
        if 'template_args' in d:
            o.template_args = d['template_args']
        if 'title' in d:
            o.title = d['title']
        if 'type' in d:
            o.type = d['type']
        return o



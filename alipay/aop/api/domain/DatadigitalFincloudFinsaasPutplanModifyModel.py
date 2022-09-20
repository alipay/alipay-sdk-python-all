#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasPutplanModifyModel(object):

    def __init__(self):
        self._activity_page = None
        self._activity_title = None
        self._benefit_desc = None
        self._bill_way = None
        self._channel_id = None
        self._crowd_ids = None
        self._customize_page = None
        self._detail_page_title = None
        self._end_time = None
        self._id = None
        self._modifier_id = None
        self._modifier_name = None
        self._name = None
        self._page_type = None
        self._pic_url = None
        self._rule_text = None
        self._start_time = None
        self._task_id = None
        self._tenant_code = None

    @property
    def activity_page(self):
        return self._activity_page

    @activity_page.setter
    def activity_page(self, value):
        self._activity_page = value
    @property
    def activity_title(self):
        return self._activity_title

    @activity_title.setter
    def activity_title(self, value):
        self._activity_title = value
    @property
    def benefit_desc(self):
        return self._benefit_desc

    @benefit_desc.setter
    def benefit_desc(self, value):
        self._benefit_desc = value
    @property
    def bill_way(self):
        return self._bill_way

    @bill_way.setter
    def bill_way(self, value):
        self._bill_way = value
    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def crowd_ids(self):
        return self._crowd_ids

    @crowd_ids.setter
    def crowd_ids(self, value):
        self._crowd_ids = value
    @property
    def customize_page(self):
        return self._customize_page

    @customize_page.setter
    def customize_page(self, value):
        self._customize_page = value
    @property
    def detail_page_title(self):
        return self._detail_page_title

    @detail_page_title.setter
    def detail_page_title(self, value):
        self._detail_page_title = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def modifier_id(self):
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, value):
        self._modifier_id = value
    @property
    def modifier_name(self):
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, value):
        self._modifier_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def page_type(self):
        return self._page_type

    @page_type.setter
    def page_type(self, value):
        self._page_type = value
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value
    @property
    def rule_text(self):
        return self._rule_text

    @rule_text.setter
    def rule_text(self, value):
        self._rule_text = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def tenant_code(self):
        return self._tenant_code

    @tenant_code.setter
    def tenant_code(self, value):
        self._tenant_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_page:
            if hasattr(self.activity_page, 'to_alipay_dict'):
                params['activity_page'] = self.activity_page.to_alipay_dict()
            else:
                params['activity_page'] = self.activity_page
        if self.activity_title:
            if hasattr(self.activity_title, 'to_alipay_dict'):
                params['activity_title'] = self.activity_title.to_alipay_dict()
            else:
                params['activity_title'] = self.activity_title
        if self.benefit_desc:
            if hasattr(self.benefit_desc, 'to_alipay_dict'):
                params['benefit_desc'] = self.benefit_desc.to_alipay_dict()
            else:
                params['benefit_desc'] = self.benefit_desc
        if self.bill_way:
            if hasattr(self.bill_way, 'to_alipay_dict'):
                params['bill_way'] = self.bill_way.to_alipay_dict()
            else:
                params['bill_way'] = self.bill_way
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.crowd_ids:
            if hasattr(self.crowd_ids, 'to_alipay_dict'):
                params['crowd_ids'] = self.crowd_ids.to_alipay_dict()
            else:
                params['crowd_ids'] = self.crowd_ids
        if self.customize_page:
            if hasattr(self.customize_page, 'to_alipay_dict'):
                params['customize_page'] = self.customize_page.to_alipay_dict()
            else:
                params['customize_page'] = self.customize_page
        if self.detail_page_title:
            if hasattr(self.detail_page_title, 'to_alipay_dict'):
                params['detail_page_title'] = self.detail_page_title.to_alipay_dict()
            else:
                params['detail_page_title'] = self.detail_page_title
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.modifier_id:
            if hasattr(self.modifier_id, 'to_alipay_dict'):
                params['modifier_id'] = self.modifier_id.to_alipay_dict()
            else:
                params['modifier_id'] = self.modifier_id
        if self.modifier_name:
            if hasattr(self.modifier_name, 'to_alipay_dict'):
                params['modifier_name'] = self.modifier_name.to_alipay_dict()
            else:
                params['modifier_name'] = self.modifier_name
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.page_type:
            if hasattr(self.page_type, 'to_alipay_dict'):
                params['page_type'] = self.page_type.to_alipay_dict()
            else:
                params['page_type'] = self.page_type
        if self.pic_url:
            if hasattr(self.pic_url, 'to_alipay_dict'):
                params['pic_url'] = self.pic_url.to_alipay_dict()
            else:
                params['pic_url'] = self.pic_url
        if self.rule_text:
            if hasattr(self.rule_text, 'to_alipay_dict'):
                params['rule_text'] = self.rule_text.to_alipay_dict()
            else:
                params['rule_text'] = self.rule_text
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.tenant_code:
            if hasattr(self.tenant_code, 'to_alipay_dict'):
                params['tenant_code'] = self.tenant_code.to_alipay_dict()
            else:
                params['tenant_code'] = self.tenant_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasPutplanModifyModel()
        if 'activity_page' in d:
            o.activity_page = d['activity_page']
        if 'activity_title' in d:
            o.activity_title = d['activity_title']
        if 'benefit_desc' in d:
            o.benefit_desc = d['benefit_desc']
        if 'bill_way' in d:
            o.bill_way = d['bill_way']
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'crowd_ids' in d:
            o.crowd_ids = d['crowd_ids']
        if 'customize_page' in d:
            o.customize_page = d['customize_page']
        if 'detail_page_title' in d:
            o.detail_page_title = d['detail_page_title']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'id' in d:
            o.id = d['id']
        if 'modifier_id' in d:
            o.modifier_id = d['modifier_id']
        if 'modifier_name' in d:
            o.modifier_name = d['modifier_name']
        if 'name' in d:
            o.name = d['name']
        if 'page_type' in d:
            o.page_type = d['page_type']
        if 'pic_url' in d:
            o.pic_url = d['pic_url']
        if 'rule_text' in d:
            o.rule_text = d['rule_text']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'tenant_code' in d:
            o.tenant_code = d['tenant_code']
        return o



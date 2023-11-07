#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdReportdataQueryModel(object):

    def __init__(self):
        self._ad_level = None
        self._alipay_pid = None
        self._biz_token = None
        self._creative_id_list = None
        self._current = None
        self._end_date = None
        self._group_id_list = None
        self._order_id_list = None
        self._page_size = None
        self._plan_id_list = None
        self._principal_tag = None
        self._query_type = None
        self._scene_type = None
        self._start_date = None

    @property
    def ad_level(self):
        return self._ad_level

    @ad_level.setter
    def ad_level(self, value):
        self._ad_level = value
    @property
    def alipay_pid(self):
        return self._alipay_pid

    @alipay_pid.setter
    def alipay_pid(self, value):
        self._alipay_pid = value
    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def creative_id_list(self):
        return self._creative_id_list

    @creative_id_list.setter
    def creative_id_list(self, value):
        if isinstance(value, list):
            self._creative_id_list = list()
            for i in value:
                self._creative_id_list.append(i)
    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def group_id_list(self):
        return self._group_id_list

    @group_id_list.setter
    def group_id_list(self, value):
        if isinstance(value, list):
            self._group_id_list = list()
            for i in value:
                self._group_id_list.append(i)
    @property
    def order_id_list(self):
        return self._order_id_list

    @order_id_list.setter
    def order_id_list(self, value):
        if isinstance(value, list):
            self._order_id_list = list()
            for i in value:
                self._order_id_list.append(i)
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def plan_id_list(self):
        return self._plan_id_list

    @plan_id_list.setter
    def plan_id_list(self, value):
        if isinstance(value, list):
            self._plan_id_list = list()
            for i in value:
                self._plan_id_list.append(i)
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.ad_level:
            if hasattr(self.ad_level, 'to_alipay_dict'):
                params['ad_level'] = self.ad_level.to_alipay_dict()
            else:
                params['ad_level'] = self.ad_level
        if self.alipay_pid:
            if hasattr(self.alipay_pid, 'to_alipay_dict'):
                params['alipay_pid'] = self.alipay_pid.to_alipay_dict()
            else:
                params['alipay_pid'] = self.alipay_pid
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.creative_id_list:
            if isinstance(self.creative_id_list, list):
                for i in range(0, len(self.creative_id_list)):
                    element = self.creative_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.creative_id_list[i] = element.to_alipay_dict()
            if hasattr(self.creative_id_list, 'to_alipay_dict'):
                params['creative_id_list'] = self.creative_id_list.to_alipay_dict()
            else:
                params['creative_id_list'] = self.creative_id_list
        if self.current:
            if hasattr(self.current, 'to_alipay_dict'):
                params['current'] = self.current.to_alipay_dict()
            else:
                params['current'] = self.current
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.group_id_list:
            if isinstance(self.group_id_list, list):
                for i in range(0, len(self.group_id_list)):
                    element = self.group_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_id_list[i] = element.to_alipay_dict()
            if hasattr(self.group_id_list, 'to_alipay_dict'):
                params['group_id_list'] = self.group_id_list.to_alipay_dict()
            else:
                params['group_id_list'] = self.group_id_list
        if self.order_id_list:
            if isinstance(self.order_id_list, list):
                for i in range(0, len(self.order_id_list)):
                    element = self.order_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_id_list[i] = element.to_alipay_dict()
            if hasattr(self.order_id_list, 'to_alipay_dict'):
                params['order_id_list'] = self.order_id_list.to_alipay_dict()
            else:
                params['order_id_list'] = self.order_id_list
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.plan_id_list:
            if isinstance(self.plan_id_list, list):
                for i in range(0, len(self.plan_id_list)):
                    element = self.plan_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.plan_id_list[i] = element.to_alipay_dict()
            if hasattr(self.plan_id_list, 'to_alipay_dict'):
                params['plan_id_list'] = self.plan_id_list.to_alipay_dict()
            else:
                params['plan_id_list'] = self.plan_id_list
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdReportdataQueryModel()
        if 'ad_level' in d:
            o.ad_level = d['ad_level']
        if 'alipay_pid' in d:
            o.alipay_pid = d['alipay_pid']
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'creative_id_list' in d:
            o.creative_id_list = d['creative_id_list']
        if 'current' in d:
            o.current = d['current']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'group_id_list' in d:
            o.group_id_list = d['group_id_list']
        if 'order_id_list' in d:
            o.order_id_list = d['order_id_list']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'plan_id_list' in d:
            o.plan_id_list = d['plan_id_list']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'query_type' in d:
            o.query_type = d['query_type']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o



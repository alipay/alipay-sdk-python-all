#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CampDetailInfo(object):

    def __init__(self):
        self._begin_time = None
        self._biz_id = None
        self._biz_type = None
        self._camp_desc = None
        self._camp_guide = None
        self._camp_id = None
        self._end_time = None
        self._ext_info = None
        self._rule_flag_list = None
        self._win_limit_daily = None
        self._win_limit_life = None

    @property
    def begin_time(self):
        return self._begin_time

    @begin_time.setter
    def begin_time(self, value):
        self._begin_time = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def camp_desc(self):
        return self._camp_desc

    @camp_desc.setter
    def camp_desc(self, value):
        self._camp_desc = value
    @property
    def camp_guide(self):
        return self._camp_guide

    @camp_guide.setter
    def camp_guide(self, value):
        self._camp_guide = value
    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def rule_flag_list(self):
        return self._rule_flag_list

    @rule_flag_list.setter
    def rule_flag_list(self, value):
        if isinstance(value, list):
            self._rule_flag_list = list()
            for i in value:
                self._rule_flag_list.append(i)
    @property
    def win_limit_daily(self):
        return self._win_limit_daily

    @win_limit_daily.setter
    def win_limit_daily(self, value):
        self._win_limit_daily = value
    @property
    def win_limit_life(self):
        return self._win_limit_life

    @win_limit_life.setter
    def win_limit_life(self, value):
        self._win_limit_life = value


    def to_alipay_dict(self):
        params = dict()
        if self.begin_time:
            if hasattr(self.begin_time, 'to_alipay_dict'):
                params['begin_time'] = self.begin_time.to_alipay_dict()
            else:
                params['begin_time'] = self.begin_time
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.camp_desc:
            if hasattr(self.camp_desc, 'to_alipay_dict'):
                params['camp_desc'] = self.camp_desc.to_alipay_dict()
            else:
                params['camp_desc'] = self.camp_desc
        if self.camp_guide:
            if hasattr(self.camp_guide, 'to_alipay_dict'):
                params['camp_guide'] = self.camp_guide.to_alipay_dict()
            else:
                params['camp_guide'] = self.camp_guide
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.rule_flag_list:
            if isinstance(self.rule_flag_list, list):
                for i in range(0, len(self.rule_flag_list)):
                    element = self.rule_flag_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rule_flag_list[i] = element.to_alipay_dict()
            if hasattr(self.rule_flag_list, 'to_alipay_dict'):
                params['rule_flag_list'] = self.rule_flag_list.to_alipay_dict()
            else:
                params['rule_flag_list'] = self.rule_flag_list
        if self.win_limit_daily:
            if hasattr(self.win_limit_daily, 'to_alipay_dict'):
                params['win_limit_daily'] = self.win_limit_daily.to_alipay_dict()
            else:
                params['win_limit_daily'] = self.win_limit_daily
        if self.win_limit_life:
            if hasattr(self.win_limit_life, 'to_alipay_dict'):
                params['win_limit_life'] = self.win_limit_life.to_alipay_dict()
            else:
                params['win_limit_life'] = self.win_limit_life
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CampDetailInfo()
        if 'begin_time' in d:
            o.begin_time = d['begin_time']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'camp_desc' in d:
            o.camp_desc = d['camp_desc']
        if 'camp_guide' in d:
            o.camp_guide = d['camp_guide']
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'rule_flag_list' in d:
            o.rule_flag_list = d['rule_flag_list']
        if 'win_limit_daily' in d:
            o.win_limit_daily = d['win_limit_daily']
        if 'win_limit_life' in d:
            o.win_limit_life = d['win_limit_life']
        return o



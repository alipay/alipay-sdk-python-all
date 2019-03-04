#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MExtInfo import MExtInfo
from alipay.aop.api.domain.MPromoInfo import MPromoInfo


class MActivityDetailInfo(object):

    def __init__(self):
        self._activity_id = None
        self._activity_status = None
        self._auto_delay_flag = None
        self._biz_scene = None
        self._creator = None
        self._creator_type = None
        self._desc = None
        self._display_status = None
        self._end_time = None
        self._ext_info = None
        self._name = None
        self._out_biz_type = None
        self._owner_id = None
        self._owner_type = None
        self._promo_info_list = None
        self._start_time = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_status(self):
        return self._activity_status

    @activity_status.setter
    def activity_status(self, value):
        self._activity_status = value
    @property
    def auto_delay_flag(self):
        return self._auto_delay_flag

    @auto_delay_flag.setter
    def auto_delay_flag(self, value):
        self._auto_delay_flag = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def creator_type(self):
        return self._creator_type

    @creator_type.setter
    def creator_type(self, value):
        self._creator_type = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def display_status(self):
        return self._display_status

    @display_status.setter
    def display_status(self, value):
        self._display_status = value
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
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, MExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(MExtInfo.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
    @property
    def owner_type(self):
        return self._owner_type

    @owner_type.setter
    def owner_type(self, value):
        self._owner_type = value
    @property
    def promo_info_list(self):
        return self._promo_info_list

    @promo_info_list.setter
    def promo_info_list(self, value):
        if isinstance(value, list):
            self._promo_info_list = list()
            for i in value:
                if isinstance(i, MPromoInfo):
                    self._promo_info_list.append(i)
                else:
                    self._promo_info_list.append(MPromoInfo.from_alipay_dict(i))
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_status:
            if hasattr(self.activity_status, 'to_alipay_dict'):
                params['activity_status'] = self.activity_status.to_alipay_dict()
            else:
                params['activity_status'] = self.activity_status
        if self.auto_delay_flag:
            if hasattr(self.auto_delay_flag, 'to_alipay_dict'):
                params['auto_delay_flag'] = self.auto_delay_flag.to_alipay_dict()
            else:
                params['auto_delay_flag'] = self.auto_delay_flag
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.creator_type:
            if hasattr(self.creator_type, 'to_alipay_dict'):
                params['creator_type'] = self.creator_type.to_alipay_dict()
            else:
                params['creator_type'] = self.creator_type
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.display_status:
            if hasattr(self.display_status, 'to_alipay_dict'):
                params['display_status'] = self.display_status.to_alipay_dict()
            else:
                params['display_status'] = self.display_status
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        if self.owner_type:
            if hasattr(self.owner_type, 'to_alipay_dict'):
                params['owner_type'] = self.owner_type.to_alipay_dict()
            else:
                params['owner_type'] = self.owner_type
        if self.promo_info_list:
            if isinstance(self.promo_info_list, list):
                for i in range(0, len(self.promo_info_list)):
                    element = self.promo_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promo_info_list[i] = element.to_alipay_dict()
            if hasattr(self.promo_info_list, 'to_alipay_dict'):
                params['promo_info_list'] = self.promo_info_list.to_alipay_dict()
            else:
                params['promo_info_list'] = self.promo_info_list
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MActivityDetailInfo()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_status' in d:
            o.activity_status = d['activity_status']
        if 'auto_delay_flag' in d:
            o.auto_delay_flag = d['auto_delay_flag']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'creator' in d:
            o.creator = d['creator']
        if 'creator_type' in d:
            o.creator_type = d['creator_type']
        if 'desc' in d:
            o.desc = d['desc']
        if 'display_status' in d:
            o.display_status = d['display_status']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'name' in d:
            o.name = d['name']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        if 'owner_type' in d:
            o.owner_type = d['owner_type']
        if 'promo_info_list' in d:
            o.promo_info_list = d['promo_info_list']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o



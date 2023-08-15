#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalopUcdpApebehaviorSyncModel(object):

    def __init__(self):
        self._action_type = None
        self._channel = None
        self._custom_id = None
        self._goods_id = None
        self._item_id_list = None
        self._item_num = None
        self._log_time = None
        self._material_id = None
        self._open_id = None
        self._order_id = None
        self._page_stay = None
        self._pay_amount = None
        self._pos = None
        self._project_id = None
        self._scene = None
        self._spm = None
        self._trace_id = None
        self._user_id = None
        self._user_id_type = None
        self._video_duration = None
        self._video_play = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def custom_id(self):
        return self._custom_id

    @custom_id.setter
    def custom_id(self, value):
        self._custom_id = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def item_id_list(self):
        return self._item_id_list

    @item_id_list.setter
    def item_id_list(self, value):
        self._item_id_list = value
    @property
    def item_num(self):
        return self._item_num

    @item_num.setter
    def item_num(self, value):
        self._item_num = value
    @property
    def log_time(self):
        return self._log_time

    @log_time.setter
    def log_time(self, value):
        self._log_time = value
    @property
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, value):
        self._material_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def page_stay(self):
        return self._page_stay

    @page_stay.setter
    def page_stay(self, value):
        self._page_stay = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def spm(self):
        return self._spm

    @spm.setter
    def spm(self, value):
        self._spm = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_id_type(self):
        return self._user_id_type

    @user_id_type.setter
    def user_id_type(self, value):
        self._user_id_type = value
    @property
    def video_duration(self):
        return self._video_duration

    @video_duration.setter
    def video_duration(self, value):
        self._video_duration = value
    @property
    def video_play(self):
        return self._video_play

    @video_play.setter
    def video_play(self, value):
        self._video_play = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.custom_id:
            if hasattr(self.custom_id, 'to_alipay_dict'):
                params['custom_id'] = self.custom_id.to_alipay_dict()
            else:
                params['custom_id'] = self.custom_id
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.item_id_list:
            if hasattr(self.item_id_list, 'to_alipay_dict'):
                params['item_id_list'] = self.item_id_list.to_alipay_dict()
            else:
                params['item_id_list'] = self.item_id_list
        if self.item_num:
            if hasattr(self.item_num, 'to_alipay_dict'):
                params['item_num'] = self.item_num.to_alipay_dict()
            else:
                params['item_num'] = self.item_num
        if self.log_time:
            if hasattr(self.log_time, 'to_alipay_dict'):
                params['log_time'] = self.log_time.to_alipay_dict()
            else:
                params['log_time'] = self.log_time
        if self.material_id:
            if hasattr(self.material_id, 'to_alipay_dict'):
                params['material_id'] = self.material_id.to_alipay_dict()
            else:
                params['material_id'] = self.material_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.page_stay:
            if hasattr(self.page_stay, 'to_alipay_dict'):
                params['page_stay'] = self.page_stay.to_alipay_dict()
            else:
                params['page_stay'] = self.page_stay
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pos:
            if hasattr(self.pos, 'to_alipay_dict'):
                params['pos'] = self.pos.to_alipay_dict()
            else:
                params['pos'] = self.pos
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.spm:
            if hasattr(self.spm, 'to_alipay_dict'):
                params['spm'] = self.spm.to_alipay_dict()
            else:
                params['spm'] = self.spm
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_id_type:
            if hasattr(self.user_id_type, 'to_alipay_dict'):
                params['user_id_type'] = self.user_id_type.to_alipay_dict()
            else:
                params['user_id_type'] = self.user_id_type
        if self.video_duration:
            if hasattr(self.video_duration, 'to_alipay_dict'):
                params['video_duration'] = self.video_duration.to_alipay_dict()
            else:
                params['video_duration'] = self.video_duration
        if self.video_play:
            if hasattr(self.video_play, 'to_alipay_dict'):
                params['video_play'] = self.video_play.to_alipay_dict()
            else:
                params['video_play'] = self.video_play
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalopUcdpApebehaviorSyncModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'channel' in d:
            o.channel = d['channel']
        if 'custom_id' in d:
            o.custom_id = d['custom_id']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'item_id_list' in d:
            o.item_id_list = d['item_id_list']
        if 'item_num' in d:
            o.item_num = d['item_num']
        if 'log_time' in d:
            o.log_time = d['log_time']
        if 'material_id' in d:
            o.material_id = d['material_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'page_stay' in d:
            o.page_stay = d['page_stay']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pos' in d:
            o.pos = d['pos']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'scene' in d:
            o.scene = d['scene']
        if 'spm' in d:
            o.spm = d['spm']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_id_type' in d:
            o.user_id_type = d['user_id_type']
        if 'video_duration' in d:
            o.video_duration = d['video_duration']
        if 'video_play' in d:
            o.video_play = d['video_play']
        return o



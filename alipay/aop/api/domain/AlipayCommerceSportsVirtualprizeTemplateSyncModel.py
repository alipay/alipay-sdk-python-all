#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsVirtualprizeTemplateSyncModel(object):

    def __init__(self):
        self._action_open = None
        self._action_url = None
        self._biz_type = None
        self._detail_picture = None
        self._detail_unreceived_picture = None
        self._detail_url = None
        self._out_prize_id = None
        self._picture = None
        self._prize_name = None
        self._prize_type = None
        self._receive_type = None
        self._rule_desc = None
        self._share_memo = None
        self._share_title = None
        self._status = None
        self._unreceived_picture = None
        self._visible_type = None

    @property
    def action_open(self):
        return self._action_open

    @action_open.setter
    def action_open(self, value):
        self._action_open = value
    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def detail_picture(self):
        return self._detail_picture

    @detail_picture.setter
    def detail_picture(self, value):
        self._detail_picture = value
    @property
    def detail_unreceived_picture(self):
        return self._detail_unreceived_picture

    @detail_unreceived_picture.setter
    def detail_unreceived_picture(self, value):
        self._detail_unreceived_picture = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def out_prize_id(self):
        return self._out_prize_id

    @out_prize_id.setter
    def out_prize_id(self, value):
        self._out_prize_id = value
    @property
    def picture(self):
        return self._picture

    @picture.setter
    def picture(self, value):
        self._picture = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value
    @property
    def receive_type(self):
        return self._receive_type

    @receive_type.setter
    def receive_type(self, value):
        self._receive_type = value
    @property
    def rule_desc(self):
        return self._rule_desc

    @rule_desc.setter
    def rule_desc(self, value):
        self._rule_desc = value
    @property
    def share_memo(self):
        return self._share_memo

    @share_memo.setter
    def share_memo(self, value):
        self._share_memo = value
    @property
    def share_title(self):
        return self._share_title

    @share_title.setter
    def share_title(self, value):
        self._share_title = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def unreceived_picture(self):
        return self._unreceived_picture

    @unreceived_picture.setter
    def unreceived_picture(self, value):
        self._unreceived_picture = value
    @property
    def visible_type(self):
        return self._visible_type

    @visible_type.setter
    def visible_type(self, value):
        self._visible_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_open:
            if hasattr(self.action_open, 'to_alipay_dict'):
                params['action_open'] = self.action_open.to_alipay_dict()
            else:
                params['action_open'] = self.action_open
        if self.action_url:
            if hasattr(self.action_url, 'to_alipay_dict'):
                params['action_url'] = self.action_url.to_alipay_dict()
            else:
                params['action_url'] = self.action_url
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.detail_picture:
            if hasattr(self.detail_picture, 'to_alipay_dict'):
                params['detail_picture'] = self.detail_picture.to_alipay_dict()
            else:
                params['detail_picture'] = self.detail_picture
        if self.detail_unreceived_picture:
            if hasattr(self.detail_unreceived_picture, 'to_alipay_dict'):
                params['detail_unreceived_picture'] = self.detail_unreceived_picture.to_alipay_dict()
            else:
                params['detail_unreceived_picture'] = self.detail_unreceived_picture
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.out_prize_id:
            if hasattr(self.out_prize_id, 'to_alipay_dict'):
                params['out_prize_id'] = self.out_prize_id.to_alipay_dict()
            else:
                params['out_prize_id'] = self.out_prize_id
        if self.picture:
            if hasattr(self.picture, 'to_alipay_dict'):
                params['picture'] = self.picture.to_alipay_dict()
            else:
                params['picture'] = self.picture
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.prize_type:
            if hasattr(self.prize_type, 'to_alipay_dict'):
                params['prize_type'] = self.prize_type.to_alipay_dict()
            else:
                params['prize_type'] = self.prize_type
        if self.receive_type:
            if hasattr(self.receive_type, 'to_alipay_dict'):
                params['receive_type'] = self.receive_type.to_alipay_dict()
            else:
                params['receive_type'] = self.receive_type
        if self.rule_desc:
            if hasattr(self.rule_desc, 'to_alipay_dict'):
                params['rule_desc'] = self.rule_desc.to_alipay_dict()
            else:
                params['rule_desc'] = self.rule_desc
        if self.share_memo:
            if hasattr(self.share_memo, 'to_alipay_dict'):
                params['share_memo'] = self.share_memo.to_alipay_dict()
            else:
                params['share_memo'] = self.share_memo
        if self.share_title:
            if hasattr(self.share_title, 'to_alipay_dict'):
                params['share_title'] = self.share_title.to_alipay_dict()
            else:
                params['share_title'] = self.share_title
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.unreceived_picture:
            if hasattr(self.unreceived_picture, 'to_alipay_dict'):
                params['unreceived_picture'] = self.unreceived_picture.to_alipay_dict()
            else:
                params['unreceived_picture'] = self.unreceived_picture
        if self.visible_type:
            if hasattr(self.visible_type, 'to_alipay_dict'):
                params['visible_type'] = self.visible_type.to_alipay_dict()
            else:
                params['visible_type'] = self.visible_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSportsVirtualprizeTemplateSyncModel()
        if 'action_open' in d:
            o.action_open = d['action_open']
        if 'action_url' in d:
            o.action_url = d['action_url']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'detail_picture' in d:
            o.detail_picture = d['detail_picture']
        if 'detail_unreceived_picture' in d:
            o.detail_unreceived_picture = d['detail_unreceived_picture']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'out_prize_id' in d:
            o.out_prize_id = d['out_prize_id']
        if 'picture' in d:
            o.picture = d['picture']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'prize_type' in d:
            o.prize_type = d['prize_type']
        if 'receive_type' in d:
            o.receive_type = d['receive_type']
        if 'rule_desc' in d:
            o.rule_desc = d['rule_desc']
        if 'share_memo' in d:
            o.share_memo = d['share_memo']
        if 'share_title' in d:
            o.share_title = d['share_title']
        if 'status' in d:
            o.status = d['status']
        if 'unreceived_picture' in d:
            o.unreceived_picture = d['unreceived_picture']
        if 'visible_type' in d:
            o.visible_type = d['visible_type']
        return o



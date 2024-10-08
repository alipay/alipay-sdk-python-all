#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JoinPanelInfo import JoinPanelInfo


class AlipayContentCommercialInteractivecoreRoundstartSyncModel(object):

    def __init__(self):
        self._biz_token = None
        self._join_panel_info = None
        self._msg_id = None
        self._round_id = None
        self._ts = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def join_panel_info(self):
        return self._join_panel_info

    @join_panel_info.setter
    def join_panel_info(self, value):
        if isinstance(value, list):
            self._join_panel_info = list()
            for i in value:
                if isinstance(i, JoinPanelInfo):
                    self._join_panel_info.append(i)
                else:
                    self._join_panel_info.append(JoinPanelInfo.from_alipay_dict(i))
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @property
    def round_id(self):
        return self._round_id

    @round_id.setter
    def round_id(self, value):
        self._round_id = value
    @property
    def ts(self):
        return self._ts

    @ts.setter
    def ts(self, value):
        self._ts = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.join_panel_info:
            if isinstance(self.join_panel_info, list):
                for i in range(0, len(self.join_panel_info)):
                    element = self.join_panel_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.join_panel_info[i] = element.to_alipay_dict()
            if hasattr(self.join_panel_info, 'to_alipay_dict'):
                params['join_panel_info'] = self.join_panel_info.to_alipay_dict()
            else:
                params['join_panel_info'] = self.join_panel_info
        if self.msg_id:
            if hasattr(self.msg_id, 'to_alipay_dict'):
                params['msg_id'] = self.msg_id.to_alipay_dict()
            else:
                params['msg_id'] = self.msg_id
        if self.round_id:
            if hasattr(self.round_id, 'to_alipay_dict'):
                params['round_id'] = self.round_id.to_alipay_dict()
            else:
                params['round_id'] = self.round_id
        if self.ts:
            if hasattr(self.ts, 'to_alipay_dict'):
                params['ts'] = self.ts.to_alipay_dict()
            else:
                params['ts'] = self.ts
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentCommercialInteractivecoreRoundstartSyncModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'join_panel_info' in d:
            o.join_panel_info = d['join_panel_info']
        if 'msg_id' in d:
            o.msg_id = d['msg_id']
        if 'round_id' in d:
            o.round_id = d['round_id']
        if 'ts' in d:
            o.ts = d['ts']
        return o



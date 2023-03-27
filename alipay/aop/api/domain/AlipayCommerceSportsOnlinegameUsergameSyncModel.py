#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsOnlinegameUsergameSyncModel(object):

    def __init__(self):
        self._game_event_id = None
        self._game_id = None
        self._gmt_complete = None
        self._gmt_join = None
        self._open_id = None
        self._out_game_event_no = None
        self._out_game_no = None
        self._out_user_game_no = None
        self._status = None
        self._user_game_id = None
        self._user_game_plate = None
        self._user_id = None
        self._user_join_type = None
        self._user_name = None
        self._user_online_detail_url = None

    @property
    def game_event_id(self):
        return self._game_event_id

    @game_event_id.setter
    def game_event_id(self, value):
        self._game_event_id = value
    @property
    def game_id(self):
        return self._game_id

    @game_id.setter
    def game_id(self, value):
        self._game_id = value
    @property
    def gmt_complete(self):
        return self._gmt_complete

    @gmt_complete.setter
    def gmt_complete(self, value):
        self._gmt_complete = value
    @property
    def gmt_join(self):
        return self._gmt_join

    @gmt_join.setter
    def gmt_join(self, value):
        self._gmt_join = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_game_event_no(self):
        return self._out_game_event_no

    @out_game_event_no.setter
    def out_game_event_no(self, value):
        self._out_game_event_no = value
    @property
    def out_game_no(self):
        return self._out_game_no

    @out_game_no.setter
    def out_game_no(self, value):
        self._out_game_no = value
    @property
    def out_user_game_no(self):
        return self._out_user_game_no

    @out_user_game_no.setter
    def out_user_game_no(self, value):
        self._out_user_game_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_game_id(self):
        return self._user_game_id

    @user_game_id.setter
    def user_game_id(self, value):
        self._user_game_id = value
    @property
    def user_game_plate(self):
        return self._user_game_plate

    @user_game_plate.setter
    def user_game_plate(self, value):
        self._user_game_plate = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_join_type(self):
        return self._user_join_type

    @user_join_type.setter
    def user_join_type(self, value):
        self._user_join_type = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_online_detail_url(self):
        return self._user_online_detail_url

    @user_online_detail_url.setter
    def user_online_detail_url(self, value):
        self._user_online_detail_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.game_event_id:
            if hasattr(self.game_event_id, 'to_alipay_dict'):
                params['game_event_id'] = self.game_event_id.to_alipay_dict()
            else:
                params['game_event_id'] = self.game_event_id
        if self.game_id:
            if hasattr(self.game_id, 'to_alipay_dict'):
                params['game_id'] = self.game_id.to_alipay_dict()
            else:
                params['game_id'] = self.game_id
        if self.gmt_complete:
            if hasattr(self.gmt_complete, 'to_alipay_dict'):
                params['gmt_complete'] = self.gmt_complete.to_alipay_dict()
            else:
                params['gmt_complete'] = self.gmt_complete
        if self.gmt_join:
            if hasattr(self.gmt_join, 'to_alipay_dict'):
                params['gmt_join'] = self.gmt_join.to_alipay_dict()
            else:
                params['gmt_join'] = self.gmt_join
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_game_event_no:
            if hasattr(self.out_game_event_no, 'to_alipay_dict'):
                params['out_game_event_no'] = self.out_game_event_no.to_alipay_dict()
            else:
                params['out_game_event_no'] = self.out_game_event_no
        if self.out_game_no:
            if hasattr(self.out_game_no, 'to_alipay_dict'):
                params['out_game_no'] = self.out_game_no.to_alipay_dict()
            else:
                params['out_game_no'] = self.out_game_no
        if self.out_user_game_no:
            if hasattr(self.out_user_game_no, 'to_alipay_dict'):
                params['out_user_game_no'] = self.out_user_game_no.to_alipay_dict()
            else:
                params['out_user_game_no'] = self.out_user_game_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.user_game_id:
            if hasattr(self.user_game_id, 'to_alipay_dict'):
                params['user_game_id'] = self.user_game_id.to_alipay_dict()
            else:
                params['user_game_id'] = self.user_game_id
        if self.user_game_plate:
            if hasattr(self.user_game_plate, 'to_alipay_dict'):
                params['user_game_plate'] = self.user_game_plate.to_alipay_dict()
            else:
                params['user_game_plate'] = self.user_game_plate
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_join_type:
            if hasattr(self.user_join_type, 'to_alipay_dict'):
                params['user_join_type'] = self.user_join_type.to_alipay_dict()
            else:
                params['user_join_type'] = self.user_join_type
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.user_online_detail_url:
            if hasattr(self.user_online_detail_url, 'to_alipay_dict'):
                params['user_online_detail_url'] = self.user_online_detail_url.to_alipay_dict()
            else:
                params['user_online_detail_url'] = self.user_online_detail_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSportsOnlinegameUsergameSyncModel()
        if 'game_event_id' in d:
            o.game_event_id = d['game_event_id']
        if 'game_id' in d:
            o.game_id = d['game_id']
        if 'gmt_complete' in d:
            o.gmt_complete = d['gmt_complete']
        if 'gmt_join' in d:
            o.gmt_join = d['gmt_join']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_game_event_no' in d:
            o.out_game_event_no = d['out_game_event_no']
        if 'out_game_no' in d:
            o.out_game_no = d['out_game_no']
        if 'out_user_game_no' in d:
            o.out_user_game_no = d['out_user_game_no']
        if 'status' in d:
            o.status = d['status']
        if 'user_game_id' in d:
            o.user_game_id = d['user_game_id']
        if 'user_game_plate' in d:
            o.user_game_plate = d['user_game_plate']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_join_type' in d:
            o.user_join_type = d['user_join_type']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_online_detail_url' in d:
            o.user_online_detail_url = d['user_online_detail_url']
        return o



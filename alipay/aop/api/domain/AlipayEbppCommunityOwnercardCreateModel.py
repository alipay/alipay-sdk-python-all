#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppCommunityOwnercardCreateModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._biz_type = None
        self._card_expired_time = None
        self._card_id = None
        self._community_id = None
        self._is_room_info_desensitization = None
        self._parent_card_id = None
        self._room_id = None
        self._room_info = None
        self._sub_biz_type = None
        self._user_type = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def card_expired_time(self):
        return self._card_expired_time

    @card_expired_time.setter
    def card_expired_time(self, value):
        self._card_expired_time = value
    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def community_id(self):
        return self._community_id

    @community_id.setter
    def community_id(self, value):
        self._community_id = value
    @property
    def is_room_info_desensitization(self):
        return self._is_room_info_desensitization

    @is_room_info_desensitization.setter
    def is_room_info_desensitization(self, value):
        self._is_room_info_desensitization = value
    @property
    def parent_card_id(self):
        return self._parent_card_id

    @parent_card_id.setter
    def parent_card_id(self, value):
        self._parent_card_id = value
    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        self._room_id = value
    @property
    def room_info(self):
        return self._room_info

    @room_info.setter
    def room_info(self, value):
        self._room_info = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.card_expired_time:
            if hasattr(self.card_expired_time, 'to_alipay_dict'):
                params['card_expired_time'] = self.card_expired_time.to_alipay_dict()
            else:
                params['card_expired_time'] = self.card_expired_time
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.community_id:
            if hasattr(self.community_id, 'to_alipay_dict'):
                params['community_id'] = self.community_id.to_alipay_dict()
            else:
                params['community_id'] = self.community_id
        if self.is_room_info_desensitization:
            if hasattr(self.is_room_info_desensitization, 'to_alipay_dict'):
                params['is_room_info_desensitization'] = self.is_room_info_desensitization.to_alipay_dict()
            else:
                params['is_room_info_desensitization'] = self.is_room_info_desensitization
        if self.parent_card_id:
            if hasattr(self.parent_card_id, 'to_alipay_dict'):
                params['parent_card_id'] = self.parent_card_id.to_alipay_dict()
            else:
                params['parent_card_id'] = self.parent_card_id
        if self.room_id:
            if hasattr(self.room_id, 'to_alipay_dict'):
                params['room_id'] = self.room_id.to_alipay_dict()
            else:
                params['room_id'] = self.room_id
        if self.room_info:
            if hasattr(self.room_info, 'to_alipay_dict'):
                params['room_info'] = self.room_info.to_alipay_dict()
            else:
                params['room_info'] = self.room_info
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppCommunityOwnercardCreateModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'card_expired_time' in d:
            o.card_expired_time = d['card_expired_time']
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'community_id' in d:
            o.community_id = d['community_id']
        if 'is_room_info_desensitization' in d:
            o.is_room_info_desensitization = d['is_room_info_desensitization']
        if 'parent_card_id' in d:
            o.parent_card_id = d['parent_card_id']
        if 'room_id' in d:
            o.room_id = d['room_id']
        if 'room_info' in d:
            o.room_info = d['room_info']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o



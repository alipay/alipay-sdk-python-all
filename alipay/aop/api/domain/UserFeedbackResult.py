#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserFeedbackResult(object):

    def __init__(self):
        self._app_name = None
        self._biz_id = None
        self._biz_level_update = None
        self._channel_id = None
        self._city = None
        self._clientproduct_version = None
        self._cls_intention = None
        self._content = None
        self._date = None
        self._device_model = None
        self._dm_subject = None
        self._emotion = None
        self._handle_status = None
        self._handle_time = None
        self._id = None
        self._last_deal_emp_id = None
        self._new_category = None
        self._new_category_name = None
        self._open_id = None
        self._os_type = None
        self._os_version = None
        self._picture = None
        self._platform_id = None
        self._replays_id = None
        self._url = None
        self._userid = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_level_update(self):
        return self._biz_level_update

    @biz_level_update.setter
    def biz_level_update(self, value):
        self._biz_level_update = value
    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def clientproduct_version(self):
        return self._clientproduct_version

    @clientproduct_version.setter
    def clientproduct_version(self, value):
        self._clientproduct_version = value
    @property
    def cls_intention(self):
        return self._cls_intention

    @cls_intention.setter
    def cls_intention(self, value):
        self._cls_intention = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def device_model(self):
        return self._device_model

    @device_model.setter
    def device_model(self, value):
        self._device_model = value
    @property
    def dm_subject(self):
        return self._dm_subject

    @dm_subject.setter
    def dm_subject(self, value):
        self._dm_subject = value
    @property
    def emotion(self):
        return self._emotion

    @emotion.setter
    def emotion(self, value):
        self._emotion = value
    @property
    def handle_status(self):
        return self._handle_status

    @handle_status.setter
    def handle_status(self, value):
        self._handle_status = value
    @property
    def handle_time(self):
        return self._handle_time

    @handle_time.setter
    def handle_time(self, value):
        self._handle_time = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def last_deal_emp_id(self):
        return self._last_deal_emp_id

    @last_deal_emp_id.setter
    def last_deal_emp_id(self, value):
        self._last_deal_emp_id = value
    @property
    def new_category(self):
        return self._new_category

    @new_category.setter
    def new_category(self, value):
        self._new_category = value
    @property
    def new_category_name(self):
        return self._new_category_name

    @new_category_name.setter
    def new_category_name(self, value):
        self._new_category_name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def os_type(self):
        return self._os_type

    @os_type.setter
    def os_type(self, value):
        self._os_type = value
    @property
    def os_version(self):
        return self._os_version

    @os_version.setter
    def os_version(self, value):
        self._os_version = value
    @property
    def picture(self):
        return self._picture

    @picture.setter
    def picture(self, value):
        self._picture = value
    @property
    def platform_id(self):
        return self._platform_id

    @platform_id.setter
    def platform_id(self, value):
        self._platform_id = value
    @property
    def replays_id(self):
        return self._replays_id

    @replays_id.setter
    def replays_id(self, value):
        self._replays_id = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
    @property
    def userid(self):
        return self._userid

    @userid.setter
    def userid(self, value):
        self._userid = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_level_update:
            if hasattr(self.biz_level_update, 'to_alipay_dict'):
                params['biz_level_update'] = self.biz_level_update.to_alipay_dict()
            else:
                params['biz_level_update'] = self.biz_level_update
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.clientproduct_version:
            if hasattr(self.clientproduct_version, 'to_alipay_dict'):
                params['clientproduct_version'] = self.clientproduct_version.to_alipay_dict()
            else:
                params['clientproduct_version'] = self.clientproduct_version
        if self.cls_intention:
            if hasattr(self.cls_intention, 'to_alipay_dict'):
                params['cls_intention'] = self.cls_intention.to_alipay_dict()
            else:
                params['cls_intention'] = self.cls_intention
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.device_model:
            if hasattr(self.device_model, 'to_alipay_dict'):
                params['device_model'] = self.device_model.to_alipay_dict()
            else:
                params['device_model'] = self.device_model
        if self.dm_subject:
            if hasattr(self.dm_subject, 'to_alipay_dict'):
                params['dm_subject'] = self.dm_subject.to_alipay_dict()
            else:
                params['dm_subject'] = self.dm_subject
        if self.emotion:
            if hasattr(self.emotion, 'to_alipay_dict'):
                params['emotion'] = self.emotion.to_alipay_dict()
            else:
                params['emotion'] = self.emotion
        if self.handle_status:
            if hasattr(self.handle_status, 'to_alipay_dict'):
                params['handle_status'] = self.handle_status.to_alipay_dict()
            else:
                params['handle_status'] = self.handle_status
        if self.handle_time:
            if hasattr(self.handle_time, 'to_alipay_dict'):
                params['handle_time'] = self.handle_time.to_alipay_dict()
            else:
                params['handle_time'] = self.handle_time
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.last_deal_emp_id:
            if hasattr(self.last_deal_emp_id, 'to_alipay_dict'):
                params['last_deal_emp_id'] = self.last_deal_emp_id.to_alipay_dict()
            else:
                params['last_deal_emp_id'] = self.last_deal_emp_id
        if self.new_category:
            if hasattr(self.new_category, 'to_alipay_dict'):
                params['new_category'] = self.new_category.to_alipay_dict()
            else:
                params['new_category'] = self.new_category
        if self.new_category_name:
            if hasattr(self.new_category_name, 'to_alipay_dict'):
                params['new_category_name'] = self.new_category_name.to_alipay_dict()
            else:
                params['new_category_name'] = self.new_category_name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.os_type:
            if hasattr(self.os_type, 'to_alipay_dict'):
                params['os_type'] = self.os_type.to_alipay_dict()
            else:
                params['os_type'] = self.os_type
        if self.os_version:
            if hasattr(self.os_version, 'to_alipay_dict'):
                params['os_version'] = self.os_version.to_alipay_dict()
            else:
                params['os_version'] = self.os_version
        if self.picture:
            if hasattr(self.picture, 'to_alipay_dict'):
                params['picture'] = self.picture.to_alipay_dict()
            else:
                params['picture'] = self.picture
        if self.platform_id:
            if hasattr(self.platform_id, 'to_alipay_dict'):
                params['platform_id'] = self.platform_id.to_alipay_dict()
            else:
                params['platform_id'] = self.platform_id
        if self.replays_id:
            if hasattr(self.replays_id, 'to_alipay_dict'):
                params['replays_id'] = self.replays_id.to_alipay_dict()
            else:
                params['replays_id'] = self.replays_id
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        if self.userid:
            if hasattr(self.userid, 'to_alipay_dict'):
                params['userid'] = self.userid.to_alipay_dict()
            else:
                params['userid'] = self.userid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserFeedbackResult()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_level_update' in d:
            o.biz_level_update = d['biz_level_update']
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'city' in d:
            o.city = d['city']
        if 'clientproduct_version' in d:
            o.clientproduct_version = d['clientproduct_version']
        if 'cls_intention' in d:
            o.cls_intention = d['cls_intention']
        if 'content' in d:
            o.content = d['content']
        if 'date' in d:
            o.date = d['date']
        if 'device_model' in d:
            o.device_model = d['device_model']
        if 'dm_subject' in d:
            o.dm_subject = d['dm_subject']
        if 'emotion' in d:
            o.emotion = d['emotion']
        if 'handle_status' in d:
            o.handle_status = d['handle_status']
        if 'handle_time' in d:
            o.handle_time = d['handle_time']
        if 'id' in d:
            o.id = d['id']
        if 'last_deal_emp_id' in d:
            o.last_deal_emp_id = d['last_deal_emp_id']
        if 'new_category' in d:
            o.new_category = d['new_category']
        if 'new_category_name' in d:
            o.new_category_name = d['new_category_name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'os_type' in d:
            o.os_type = d['os_type']
        if 'os_version' in d:
            o.os_version = d['os_version']
        if 'picture' in d:
            o.picture = d['picture']
        if 'platform_id' in d:
            o.platform_id = d['platform_id']
        if 'replays_id' in d:
            o.replays_id = d['replays_id']
        if 'url' in d:
            o.url = d['url']
        if 'userid' in d:
            o.userid = d['userid']
        return o



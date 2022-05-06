#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContextMap import ContextMap
from alipay.aop.api.domain.PaperSealDisplayOpenApiDTO import PaperSealDisplayOpenApiDTO
from alipay.aop.api.domain.PeopleOpenApiDTO import PeopleOpenApiDTO


class PaperSealExtOpenApiRequest(object):

    def __init__(self):
        self._context = None
        self._copies_num = None
        self._delay_days = None
        self._delivery_type = None
        self._display_info = None
        self._expect_finish_date = None
        self._only_notify_sender = None
        self._private_level = None
        self._seal_file_type = None
        self._sender = None
        self._tags = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        if isinstance(value, ContextMap):
            self._context = value
        else:
            self._context = ContextMap.from_alipay_dict(value)
    @property
    def copies_num(self):
        return self._copies_num

    @copies_num.setter
    def copies_num(self, value):
        self._copies_num = value
    @property
    def delay_days(self):
        return self._delay_days

    @delay_days.setter
    def delay_days(self, value):
        self._delay_days = value
    @property
    def delivery_type(self):
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, value):
        self._delivery_type = value
    @property
    def display_info(self):
        return self._display_info

    @display_info.setter
    def display_info(self, value):
        if isinstance(value, list):
            self._display_info = list()
            for i in value:
                if isinstance(i, PaperSealDisplayOpenApiDTO):
                    self._display_info.append(i)
                else:
                    self._display_info.append(PaperSealDisplayOpenApiDTO.from_alipay_dict(i))
    @property
    def expect_finish_date(self):
        return self._expect_finish_date

    @expect_finish_date.setter
    def expect_finish_date(self, value):
        self._expect_finish_date = value
    @property
    def only_notify_sender(self):
        return self._only_notify_sender

    @only_notify_sender.setter
    def only_notify_sender(self, value):
        self._only_notify_sender = value
    @property
    def private_level(self):
        return self._private_level

    @private_level.setter
    def private_level(self, value):
        self._private_level = value
    @property
    def seal_file_type(self):
        return self._seal_file_type

    @seal_file_type.setter
    def seal_file_type(self, value):
        self._seal_file_type = value
    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, value):
        if isinstance(value, PeopleOpenApiDTO):
            self._sender = value
        else:
            self._sender = PeopleOpenApiDTO.from_alipay_dict(value)
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, list):
            self._tags = list()
            for i in value:
                self._tags.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.context:
            if hasattr(self.context, 'to_alipay_dict'):
                params['context'] = self.context.to_alipay_dict()
            else:
                params['context'] = self.context
        if self.copies_num:
            if hasattr(self.copies_num, 'to_alipay_dict'):
                params['copies_num'] = self.copies_num.to_alipay_dict()
            else:
                params['copies_num'] = self.copies_num
        if self.delay_days:
            if hasattr(self.delay_days, 'to_alipay_dict'):
                params['delay_days'] = self.delay_days.to_alipay_dict()
            else:
                params['delay_days'] = self.delay_days
        if self.delivery_type:
            if hasattr(self.delivery_type, 'to_alipay_dict'):
                params['delivery_type'] = self.delivery_type.to_alipay_dict()
            else:
                params['delivery_type'] = self.delivery_type
        if self.display_info:
            if isinstance(self.display_info, list):
                for i in range(0, len(self.display_info)):
                    element = self.display_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.display_info[i] = element.to_alipay_dict()
            if hasattr(self.display_info, 'to_alipay_dict'):
                params['display_info'] = self.display_info.to_alipay_dict()
            else:
                params['display_info'] = self.display_info
        if self.expect_finish_date:
            if hasattr(self.expect_finish_date, 'to_alipay_dict'):
                params['expect_finish_date'] = self.expect_finish_date.to_alipay_dict()
            else:
                params['expect_finish_date'] = self.expect_finish_date
        if self.only_notify_sender:
            if hasattr(self.only_notify_sender, 'to_alipay_dict'):
                params['only_notify_sender'] = self.only_notify_sender.to_alipay_dict()
            else:
                params['only_notify_sender'] = self.only_notify_sender
        if self.private_level:
            if hasattr(self.private_level, 'to_alipay_dict'):
                params['private_level'] = self.private_level.to_alipay_dict()
            else:
                params['private_level'] = self.private_level
        if self.seal_file_type:
            if hasattr(self.seal_file_type, 'to_alipay_dict'):
                params['seal_file_type'] = self.seal_file_type.to_alipay_dict()
            else:
                params['seal_file_type'] = self.seal_file_type
        if self.sender:
            if hasattr(self.sender, 'to_alipay_dict'):
                params['sender'] = self.sender.to_alipay_dict()
            else:
                params['sender'] = self.sender
        if self.tags:
            if isinstance(self.tags, list):
                for i in range(0, len(self.tags)):
                    element = self.tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tags[i] = element.to_alipay_dict()
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaperSealExtOpenApiRequest()
        if 'context' in d:
            o.context = d['context']
        if 'copies_num' in d:
            o.copies_num = d['copies_num']
        if 'delay_days' in d:
            o.delay_days = d['delay_days']
        if 'delivery_type' in d:
            o.delivery_type = d['delivery_type']
        if 'display_info' in d:
            o.display_info = d['display_info']
        if 'expect_finish_date' in d:
            o.expect_finish_date = d['expect_finish_date']
        if 'only_notify_sender' in d:
            o.only_notify_sender = d['only_notify_sender']
        if 'private_level' in d:
            o.private_level = d['private_level']
        if 'seal_file_type' in d:
            o.seal_file_type = d['seal_file_type']
        if 'sender' in d:
            o.sender = d['sender']
        if 'tags' in d:
            o.tags = d['tags']
        return o



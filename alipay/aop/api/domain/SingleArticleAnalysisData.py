#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SingleArticleAnalysisData(object):

    def __init__(self):
        self._avg_read_time = None
        self._date = None
        self._deliver_user_cnt = None
        self._expose_user_cnt = None
        self._praise_user_cnt = None
        self._read_user_cnt = None
        self._reply_user_cnt = None
        self._share_user_cnt = None
        self._title = None

    @property
    def avg_read_time(self):
        return self._avg_read_time

    @avg_read_time.setter
    def avg_read_time(self, value):
        self._avg_read_time = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def deliver_user_cnt(self):
        return self._deliver_user_cnt

    @deliver_user_cnt.setter
    def deliver_user_cnt(self, value):
        self._deliver_user_cnt = value
    @property
    def expose_user_cnt(self):
        return self._expose_user_cnt

    @expose_user_cnt.setter
    def expose_user_cnt(self, value):
        self._expose_user_cnt = value
    @property
    def praise_user_cnt(self):
        return self._praise_user_cnt

    @praise_user_cnt.setter
    def praise_user_cnt(self, value):
        self._praise_user_cnt = value
    @property
    def read_user_cnt(self):
        return self._read_user_cnt

    @read_user_cnt.setter
    def read_user_cnt(self, value):
        self._read_user_cnt = value
    @property
    def reply_user_cnt(self):
        return self._reply_user_cnt

    @reply_user_cnt.setter
    def reply_user_cnt(self, value):
        self._reply_user_cnt = value
    @property
    def share_user_cnt(self):
        return self._share_user_cnt

    @share_user_cnt.setter
    def share_user_cnt(self, value):
        self._share_user_cnt = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.avg_read_time:
            if hasattr(self.avg_read_time, 'to_alipay_dict'):
                params['avg_read_time'] = self.avg_read_time.to_alipay_dict()
            else:
                params['avg_read_time'] = self.avg_read_time
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.deliver_user_cnt:
            if hasattr(self.deliver_user_cnt, 'to_alipay_dict'):
                params['deliver_user_cnt'] = self.deliver_user_cnt.to_alipay_dict()
            else:
                params['deliver_user_cnt'] = self.deliver_user_cnt
        if self.expose_user_cnt:
            if hasattr(self.expose_user_cnt, 'to_alipay_dict'):
                params['expose_user_cnt'] = self.expose_user_cnt.to_alipay_dict()
            else:
                params['expose_user_cnt'] = self.expose_user_cnt
        if self.praise_user_cnt:
            if hasattr(self.praise_user_cnt, 'to_alipay_dict'):
                params['praise_user_cnt'] = self.praise_user_cnt.to_alipay_dict()
            else:
                params['praise_user_cnt'] = self.praise_user_cnt
        if self.read_user_cnt:
            if hasattr(self.read_user_cnt, 'to_alipay_dict'):
                params['read_user_cnt'] = self.read_user_cnt.to_alipay_dict()
            else:
                params['read_user_cnt'] = self.read_user_cnt
        if self.reply_user_cnt:
            if hasattr(self.reply_user_cnt, 'to_alipay_dict'):
                params['reply_user_cnt'] = self.reply_user_cnt.to_alipay_dict()
            else:
                params['reply_user_cnt'] = self.reply_user_cnt
        if self.share_user_cnt:
            if hasattr(self.share_user_cnt, 'to_alipay_dict'):
                params['share_user_cnt'] = self.share_user_cnt.to_alipay_dict()
            else:
                params['share_user_cnt'] = self.share_user_cnt
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SingleArticleAnalysisData()
        if 'avg_read_time' in d:
            o.avg_read_time = d['avg_read_time']
        if 'date' in d:
            o.date = d['date']
        if 'deliver_user_cnt' in d:
            o.deliver_user_cnt = d['deliver_user_cnt']
        if 'expose_user_cnt' in d:
            o.expose_user_cnt = d['expose_user_cnt']
        if 'praise_user_cnt' in d:
            o.praise_user_cnt = d['praise_user_cnt']
        if 'read_user_cnt' in d:
            o.read_user_cnt = d['read_user_cnt']
        if 'reply_user_cnt' in d:
            o.reply_user_cnt = d['reply_user_cnt']
        if 'share_user_cnt' in d:
            o.share_user_cnt = d['share_user_cnt']
        if 'title' in d:
            o.title = d['title']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DoctorContentStatisticalResult(object):

    def __init__(self):
        self._article_pv_total = None
        self._article_total = None
        self._live_pv_total = None
        self._live_total = None
        self._merchant_doctor_id = None
        self._praise_count = None
        self._video_pv_total = None
        self._video_total = None

    @property
    def article_pv_total(self):
        return self._article_pv_total

    @article_pv_total.setter
    def article_pv_total(self, value):
        self._article_pv_total = value
    @property
    def article_total(self):
        return self._article_total

    @article_total.setter
    def article_total(self, value):
        self._article_total = value
    @property
    def live_pv_total(self):
        return self._live_pv_total

    @live_pv_total.setter
    def live_pv_total(self, value):
        self._live_pv_total = value
    @property
    def live_total(self):
        return self._live_total

    @live_total.setter
    def live_total(self, value):
        self._live_total = value
    @property
    def merchant_doctor_id(self):
        return self._merchant_doctor_id

    @merchant_doctor_id.setter
    def merchant_doctor_id(self, value):
        self._merchant_doctor_id = value
    @property
    def praise_count(self):
        return self._praise_count

    @praise_count.setter
    def praise_count(self, value):
        self._praise_count = value
    @property
    def video_pv_total(self):
        return self._video_pv_total

    @video_pv_total.setter
    def video_pv_total(self, value):
        self._video_pv_total = value
    @property
    def video_total(self):
        return self._video_total

    @video_total.setter
    def video_total(self, value):
        self._video_total = value


    def to_alipay_dict(self):
        params = dict()
        if self.article_pv_total:
            if hasattr(self.article_pv_total, 'to_alipay_dict'):
                params['article_pv_total'] = self.article_pv_total.to_alipay_dict()
            else:
                params['article_pv_total'] = self.article_pv_total
        if self.article_total:
            if hasattr(self.article_total, 'to_alipay_dict'):
                params['article_total'] = self.article_total.to_alipay_dict()
            else:
                params['article_total'] = self.article_total
        if self.live_pv_total:
            if hasattr(self.live_pv_total, 'to_alipay_dict'):
                params['live_pv_total'] = self.live_pv_total.to_alipay_dict()
            else:
                params['live_pv_total'] = self.live_pv_total
        if self.live_total:
            if hasattr(self.live_total, 'to_alipay_dict'):
                params['live_total'] = self.live_total.to_alipay_dict()
            else:
                params['live_total'] = self.live_total
        if self.merchant_doctor_id:
            if hasattr(self.merchant_doctor_id, 'to_alipay_dict'):
                params['merchant_doctor_id'] = self.merchant_doctor_id.to_alipay_dict()
            else:
                params['merchant_doctor_id'] = self.merchant_doctor_id
        if self.praise_count:
            if hasattr(self.praise_count, 'to_alipay_dict'):
                params['praise_count'] = self.praise_count.to_alipay_dict()
            else:
                params['praise_count'] = self.praise_count
        if self.video_pv_total:
            if hasattr(self.video_pv_total, 'to_alipay_dict'):
                params['video_pv_total'] = self.video_pv_total.to_alipay_dict()
            else:
                params['video_pv_total'] = self.video_pv_total
        if self.video_total:
            if hasattr(self.video_total, 'to_alipay_dict'):
                params['video_total'] = self.video_total.to_alipay_dict()
            else:
                params['video_total'] = self.video_total
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DoctorContentStatisticalResult()
        if 'article_pv_total' in d:
            o.article_pv_total = d['article_pv_total']
        if 'article_total' in d:
            o.article_total = d['article_total']
        if 'live_pv_total' in d:
            o.live_pv_total = d['live_pv_total']
        if 'live_total' in d:
            o.live_total = d['live_total']
        if 'merchant_doctor_id' in d:
            o.merchant_doctor_id = d['merchant_doctor_id']
        if 'praise_count' in d:
            o.praise_count = d['praise_count']
        if 'video_pv_total' in d:
            o.video_pv_total = d['video_pv_total']
        if 'video_total' in d:
            o.video_total = d['video_total']
        return o



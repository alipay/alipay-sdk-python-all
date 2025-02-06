#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MarkDTO(object):

    def __init__(self):
        self._pic_urls = None
        self._video_card_vo = None

    @property
    def pic_urls(self):
        return self._pic_urls

    @pic_urls.setter
    def pic_urls(self, value):
        if isinstance(value, list):
            self._pic_urls = list()
            for i in value:
                self._pic_urls.append(i)
    @property
    def video_card_vo(self):
        return self._video_card_vo

    @video_card_vo.setter
    def video_card_vo(self, value):
        if isinstance(value, list):
            self._video_card_vo = list()
            for i in value:
                self._video_card_vo.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.pic_urls:
            if isinstance(self.pic_urls, list):
                for i in range(0, len(self.pic_urls)):
                    element = self.pic_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pic_urls[i] = element.to_alipay_dict()
            if hasattr(self.pic_urls, 'to_alipay_dict'):
                params['pic_urls'] = self.pic_urls.to_alipay_dict()
            else:
                params['pic_urls'] = self.pic_urls
        if self.video_card_vo:
            if isinstance(self.video_card_vo, list):
                for i in range(0, len(self.video_card_vo)):
                    element = self.video_card_vo[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.video_card_vo[i] = element.to_alipay_dict()
            if hasattr(self.video_card_vo, 'to_alipay_dict'):
                params['video_card_vo'] = self.video_card_vo.to_alipay_dict()
            else:
                params['video_card_vo'] = self.video_card_vo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MarkDTO()
        if 'pic_urls' in d:
            o.pic_urls = d['pic_urls']
        if 'video_card_vo' in d:
            o.video_card_vo = d['video_card_vo']
        return o



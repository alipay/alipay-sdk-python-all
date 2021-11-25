#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SourceMediaInfo import SourceMediaInfo
from alipay.aop.api.domain.SourceOffer import SourceOffer


class SourceContentInfo(object):

    def __init__(self):
        self._content_id = None
        self._link = None
        self._source_author = None
        self._source_link = None
        self._source_media_infos = None
        self._source_offers = None
        self._source_publish_date = None
        self._source_status = None
        self._source_summary = None
        self._source_title = None
        self._source_type = None
        self._special_tags = None

    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    @property
    def source_author(self):
        return self._source_author

    @source_author.setter
    def source_author(self, value):
        self._source_author = value
    @property
    def source_link(self):
        return self._source_link

    @source_link.setter
    def source_link(self, value):
        self._source_link = value
    @property
    def source_media_infos(self):
        return self._source_media_infos

    @source_media_infos.setter
    def source_media_infos(self, value):
        if isinstance(value, list):
            self._source_media_infos = list()
            for i in value:
                if isinstance(i, SourceMediaInfo):
                    self._source_media_infos.append(i)
                else:
                    self._source_media_infos.append(SourceMediaInfo.from_alipay_dict(i))
    @property
    def source_offers(self):
        return self._source_offers

    @source_offers.setter
    def source_offers(self, value):
        if isinstance(value, list):
            self._source_offers = list()
            for i in value:
                if isinstance(i, SourceOffer):
                    self._source_offers.append(i)
                else:
                    self._source_offers.append(SourceOffer.from_alipay_dict(i))
    @property
    def source_publish_date(self):
        return self._source_publish_date

    @source_publish_date.setter
    def source_publish_date(self, value):
        self._source_publish_date = value
    @property
    def source_status(self):
        return self._source_status

    @source_status.setter
    def source_status(self, value):
        self._source_status = value
    @property
    def source_summary(self):
        return self._source_summary

    @source_summary.setter
    def source_summary(self, value):
        self._source_summary = value
    @property
    def source_title(self):
        return self._source_title

    @source_title.setter
    def source_title(self, value):
        self._source_title = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value
    @property
    def special_tags(self):
        return self._special_tags

    @special_tags.setter
    def special_tags(self, value):
        if isinstance(value, list):
            self._special_tags = list()
            for i in value:
                self._special_tags.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.link:
            if hasattr(self.link, 'to_alipay_dict'):
                params['link'] = self.link.to_alipay_dict()
            else:
                params['link'] = self.link
        if self.source_author:
            if hasattr(self.source_author, 'to_alipay_dict'):
                params['source_author'] = self.source_author.to_alipay_dict()
            else:
                params['source_author'] = self.source_author
        if self.source_link:
            if hasattr(self.source_link, 'to_alipay_dict'):
                params['source_link'] = self.source_link.to_alipay_dict()
            else:
                params['source_link'] = self.source_link
        if self.source_media_infos:
            if isinstance(self.source_media_infos, list):
                for i in range(0, len(self.source_media_infos)):
                    element = self.source_media_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.source_media_infos[i] = element.to_alipay_dict()
            if hasattr(self.source_media_infos, 'to_alipay_dict'):
                params['source_media_infos'] = self.source_media_infos.to_alipay_dict()
            else:
                params['source_media_infos'] = self.source_media_infos
        if self.source_offers:
            if isinstance(self.source_offers, list):
                for i in range(0, len(self.source_offers)):
                    element = self.source_offers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.source_offers[i] = element.to_alipay_dict()
            if hasattr(self.source_offers, 'to_alipay_dict'):
                params['source_offers'] = self.source_offers.to_alipay_dict()
            else:
                params['source_offers'] = self.source_offers
        if self.source_publish_date:
            if hasattr(self.source_publish_date, 'to_alipay_dict'):
                params['source_publish_date'] = self.source_publish_date.to_alipay_dict()
            else:
                params['source_publish_date'] = self.source_publish_date
        if self.source_status:
            if hasattr(self.source_status, 'to_alipay_dict'):
                params['source_status'] = self.source_status.to_alipay_dict()
            else:
                params['source_status'] = self.source_status
        if self.source_summary:
            if hasattr(self.source_summary, 'to_alipay_dict'):
                params['source_summary'] = self.source_summary.to_alipay_dict()
            else:
                params['source_summary'] = self.source_summary
        if self.source_title:
            if hasattr(self.source_title, 'to_alipay_dict'):
                params['source_title'] = self.source_title.to_alipay_dict()
            else:
                params['source_title'] = self.source_title
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        if self.special_tags:
            if isinstance(self.special_tags, list):
                for i in range(0, len(self.special_tags)):
                    element = self.special_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.special_tags[i] = element.to_alipay_dict()
            if hasattr(self.special_tags, 'to_alipay_dict'):
                params['special_tags'] = self.special_tags.to_alipay_dict()
            else:
                params['special_tags'] = self.special_tags
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SourceContentInfo()
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'link' in d:
            o.link = d['link']
        if 'source_author' in d:
            o.source_author = d['source_author']
        if 'source_link' in d:
            o.source_link = d['source_link']
        if 'source_media_infos' in d:
            o.source_media_infos = d['source_media_infos']
        if 'source_offers' in d:
            o.source_offers = d['source_offers']
        if 'source_publish_date' in d:
            o.source_publish_date = d['source_publish_date']
        if 'source_status' in d:
            o.source_status = d['source_status']
        if 'source_summary' in d:
            o.source_summary = d['source_summary']
        if 'source_title' in d:
            o.source_title = d['source_title']
        if 'source_type' in d:
            o.source_type = d['source_type']
        if 'special_tags' in d:
            o.special_tags = d['special_tags']
        return o



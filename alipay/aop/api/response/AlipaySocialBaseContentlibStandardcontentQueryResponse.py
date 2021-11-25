#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SourceMediaInfo import SourceMediaInfo
from alipay.aop.api.domain.SourceOffer import SourceOffer


class AlipaySocialBaseContentlibStandardcontentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseContentlibStandardcontentQueryResponse, self).__init__()
        self._content_id = None
        self._link = None
        self._source_author = None
        self._source_content = None
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
    def source_content(self):
        return self._source_content

    @source_content.setter
    def source_content(self, value):
        self._source_content = value
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

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseContentlibStandardcontentQueryResponse, self).parse_response_content(response_content)
        if 'content_id' in response:
            self.content_id = response['content_id']
        if 'link' in response:
            self.link = response['link']
        if 'source_author' in response:
            self.source_author = response['source_author']
        if 'source_content' in response:
            self.source_content = response['source_content']
        if 'source_link' in response:
            self.source_link = response['source_link']
        if 'source_media_infos' in response:
            self.source_media_infos = response['source_media_infos']
        if 'source_offers' in response:
            self.source_offers = response['source_offers']
        if 'source_publish_date' in response:
            self.source_publish_date = response['source_publish_date']
        if 'source_status' in response:
            self.source_status = response['source_status']
        if 'source_summary' in response:
            self.source_summary = response['source_summary']
        if 'source_title' in response:
            self.source_title = response['source_title']
        if 'source_type' in response:
            self.source_type = response['source_type']
        if 'special_tags' in response:
            self.special_tags = response['special_tags']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ArchiveFaceInfo import ArchiveFaceInfo


class AlipayUserAntarchiveFaceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAntarchiveFaceQueryResponse, self).__init__()
        self._archive_face_list = None
        self._local_usable = None
        self._remote_usable = None

    @property
    def archive_face_list(self):
        return self._archive_face_list

    @archive_face_list.setter
    def archive_face_list(self, value):
        if isinstance(value, list):
            self._archive_face_list = list()
            for i in value:
                if isinstance(i, ArchiveFaceInfo):
                    self._archive_face_list.append(i)
                else:
                    self._archive_face_list.append(ArchiveFaceInfo.from_alipay_dict(i))
    @property
    def local_usable(self):
        return self._local_usable

    @local_usable.setter
    def local_usable(self, value):
        self._local_usable = value
    @property
    def remote_usable(self):
        return self._remote_usable

    @remote_usable.setter
    def remote_usable(self, value):
        self._remote_usable = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAntarchiveFaceQueryResponse, self).parse_response_content(response_content)
        if 'archive_face_list' in response:
            self.archive_face_list = response['archive_face_list']
        if 'local_usable' in response:
            self.local_usable = response['local_usable']
        if 'remote_usable' in response:
            self.remote_usable = response['remote_usable']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ArchiveFaceInfo import ArchiveFaceInfo


class AlipayUserAntarchiveFaceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAntarchiveFaceQueryResponse, self).__init__()
        self._archive_face_list = None

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

    def parse_response_content(self, response_content):
        response = super(AlipayUserAntarchiveFaceQueryResponse, self).parse_response_content(response_content)
        if 'archive_face_list' in response:
            self.archive_face_list = response['archive_face_list']

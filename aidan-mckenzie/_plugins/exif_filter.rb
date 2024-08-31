require 'exifr/jpeg'

module Jekyll
  module ExifFilter
    def exif_tag(file, tag)
      return unless File.exist?(file)

      exif = EXIFR::JPEG.new(file)
      exif.respond_to?(tag) ? exif.send(tag) : nil
    end
  end
end

Liquid::Template.register_filter(Jekyll::ExifFilter)

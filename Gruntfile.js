module.exports = function(grunt) {
 
  grunt.registerTask('watch', [ 'watch' ]);
 
  grunt.initConfig({
    less: {
      style: {
        files: {
          "starter/static/css/screen.css": "starter/static/less/freelancer.less"
        }
      }
    },
    watch: {
      html: {
        files: ['starter/starter/templates/*/*', 'starter/pager/templates/*/*'],
        options: {
          livereload: true,
        }
      },
      css: {
        files: ['starter/static/less/*.less'],
        tasks: ['less:style'],
        options: {
          livereload: true,
        }
      }
    }
  });
 
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-watch');
 
};

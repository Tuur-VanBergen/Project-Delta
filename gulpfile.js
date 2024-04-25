import gulp from 'gulp';

// Needed for development (gulp)
import browserSync from 'browser-sync';
import plumber from 'gulp-plumber';
import notify from 'gulp-notify';
import newer from 'gulp-newer';
import sass from 'gulp-dart-sass';
import prefix from 'gulp-autoprefixer';
import sourcemaps from 'gulp-sourcemaps';
import gcmqp from 'gulp-css-mqpacker';

// Needed for production (gulp build)
import { deleteAsync } from 'del';

// Copy Bootstrap JS-file
gulp.task('copy-js', () =>
    gulp
        .src(['node_modules/bootstrap/dist/js/bootstrap.bundle.min.js'])
        .pipe(newer('./src/js'))
        .pipe(notify({ message: 'Copy JS files' }))
        .pipe(gulp.dest('./src/js'))
);


// Live-reload the browser
gulp.task('browser-sync', () => {
    browserSync.init({
        startPath: '/index.html',
        port: 7777,
        server: {
            baseDir: './src',
            directory: true,
        },
        ui: {
            port: 7779,
        },
    });
    gulp.watch('./src/**/*.{html,css,js}').on('change', browserSync.reload);
});

// Delete all files and folders inside the dist folder
gulp.task('clean', () => deleteAsync(['dist/**/*']));

// Copy files from ./src to ./dist
gulp.task('copy', () => gulp.src('./src/**/*').pipe(gulp.dest('./dist')));


gulp.task('build', gulp.series('clean', 'copy-js', 'copy'));
gulp.task('default', gulp.series('copy-js', 'browser-sync'));
